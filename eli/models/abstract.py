from abc import ABC, abstractmethod


class GenericAPI(ABC):
    """Abstract class to handle queries to LLM APIs.
    
    Each subclass must be initialized with a 'model' and a 'prompt' which 
    are used in the API processing functions."""

    def __init__(self, model, prompt) -> None:
        self.model = model
        self.prompt = prompt

    @abstractmethod
    def preprocess(self) -> str:
        """Runs preprocessing steps on the prompt to prepare it for the API"""
        pass

    @abstractmethod
    def predict(self, preprocessed_prompt: str) -> str:
        """Run the prediction/query function using the preprocessed prompt"""
        pass
    
    @abstractmethod
    def postprocess(self, prediction: str) -> str:
        """Runs postprocessing steps on the prediction from the API and returns the modified prediction"""
        pass

    def query(self) -> str:
        """Top-level function to run a query against the API. 
        Calls the preprocess, predict, and postprocess functions."""
        preprocessed_prompt = self.preprocess()
        prediction = self.predict(preprocessed_prompt)
        return self.postprocess(prediction)
