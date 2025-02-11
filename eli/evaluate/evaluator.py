import traceback
from typing import Callable, Union, cast

from weave import Evaluation, op as weave_op
from weave.trace.errors import OpCallError
from weave.trace.env import get_weave_parallelism
from weave.flow.dataset import Dataset
from weave.flow.model import Model
from weave.flow.scorer import get_scorer_attributes
from weave.flow import util


class Evaluator(Evaluation):
    @weave_op()
    async def evaluate(
        self,
        model: Union[Callable, Model],
        return_rows: bool = False,
        workers: int = 1
    ) -> dict | tuple[dict, list]:
        async def eval_example(example: dict) -> dict:
            # Function that processes each example
            try:
                eval_row = await self.predict_and_score(model, example)
            except OpCallError as e:
                raise e
            except Exception:
                print("Predict and score failed")
                traceback.print_exc()
                return {"model_output": None, "scores": {}}
            return eval_row

        eval_rows = []
        n_complete = 0
        dataset = cast(Dataset, self.dataset)
        _rows = dataset.rows
        trial_rows = list(_rows) * self.trials

        # Process each row with a semaphore-controlled task
        async for _, eval_row in util.async_foreach(
            sequence=trial_rows, func=eval_example, max_concurrent_tasks=workers
        ):
            n_complete += 1
            print(f"Evaluated {n_complete} of {len(trial_rows)} examples")
            if eval_row is None:
                eval_row = {"model_output": None, "scores": {}}
            if eval_row["scores"] is None:
                eval_row["scores"] = {}
            for scorer in self.scorers or []:
                scorer_name, _, _ = get_scorer_attributes(scorer)
                if scorer_name not in eval_row["scores"]:
                    eval_row["scores"][scorer_name] = {}
            print("adding row")
            print(eval_row)
            eval_rows.append(eval_row)

        # Summarize the results after all rows have been evaluated

#        import pdb
#        pdb.set_trace()
        
        summary = await self.summarize(eval_rows)
        if return_rows:
            return summary, eval_rows
        return summary
