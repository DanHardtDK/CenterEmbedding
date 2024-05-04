from time import sleep
from abc import ABC
from typing import final

from langchain.schema import AIMessage
from openai import RateLimitError, Timeout, APIError, APIStatusError, APIConnectionError

from utils.loggers import logger


class GenericAPI(ABC):

    """Abstract class to handle queries to LLM APIs.
    Not to be confused with the APIHandler class, which
    is where the model and template are specified."""

    def __init__(self) -> None:
        super().__init__()

    @final
    def _run_query(self, sleep_seconds: int = 5, **kwargs) -> str:
        """Run the query function, and handle rate limit errors"""

        try:
            prompt: str = self.template.format_query(**kwargs)
            _prediction: AIMessage = self.model.invoke(prompt)
            prediction: str = self.postprocess(_prediction)
            print(prediction)

        except (RateLimitError, Timeout, APIStatusError, APIError, APIConnectionError) as e:
            logger.info(f"{e.__class__.__name__}: Waiting {sleep_seconds} seconds...")
            sleep(sleep_seconds)
            return self._run_query(**kwargs)

        finally:
            logger.info(
                "-> PROMPT:\n<SYSTEM PROMPT>\n\n"
                + f"{kwargs['context']}\n{kwargs['question']}\n\n"
            )
            return prediction

    @final
    def evaluate(self, prediction: str, true_answer: str) -> bool:
        """Evaluate whether the true answer appears at the start
        of the last line or at the end of the prediction."""

        # ignore quotes around prediction and true_answer if any
        prediction = prediction.strip("'\"")
        prediction = prediction.strip(".")
        prediction = prediction.lower()

        true_answer = true_answer.strip("'\"")
        true_answer = true_answer.strip(".")
        true_answer = true_answer.lower()

        print(prediction, true_answer)
        #        pdb.set_trace()
        # Check if the true answer appears at the end of the prediction
        if prediction.endswith(true_answer):
            return True
        # Check if the true answer appears at the start of the last line
        elif prediction.rsplit("\n", 1)[-1].strip().startswith(true_answer):
            return True

        return False

    @final
    def query(self, true_answer: str, **kwargs) -> bool:
        """Top-level function to run a query and evaluate the outcome"""

        prediction: str = self._run_query(**kwargs)
        correct_result: bool = self.evaluate(prediction, true_answer)

        logger.info(
            f"MODEL ANSWER:\n{prediction}\n"
            + f"{'-'*10}\n"
            + f"Correct is {true_answer} -> Prediction is {correct_result}\n"
            + "#" * 30
            + "\n"
        )
        return correct_result

    @final
    def postprocess(self, prediction: AIMessage | str) -> str:
        """Runs postprocessing steps on the prediction
        from the API and returns the prediction as a string

        Args:
            prediction (AIMessage): The prediction from the API
        Returns:
            str: The prediction as a string
        """

        if not isinstance(prediction, str):
            prediction = prediction.content

        return prediction.rstrip(".").strip()
