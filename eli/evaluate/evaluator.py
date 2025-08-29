import traceback
from typing import Callable, Union, cast, Any, Dict, List

# Use our light-weight compat layer instead of Weave
from eli.compat.weave_compat import (
    Evaluation,
    Dataset,
    Model,
    get_scorer_attributes,
    util,
)

class Evaluator(Evaluation):
    @weave_op()  # now a NO-OP; leaves this as a plain async method
    async def evaluate(
        self,
        model: Union[Callable, Model],
        return_rows: bool = False,
        workers: int = 1,
    ) -> dict | tuple[dict, list]:
        async def eval_example(example: dict) -> dict:
            # Function that processes each example
            try:
                eval_row = await self.predict_and_score(model, example)
            except Exception:
                raise e
            except Exception:
                print("Predict and score failed")
                traceback.print_exc()
                return {"model_output": None, "scores": {}}
            return eval_row

        eval_rows: List[Dict[str, Any]] = []
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
            if eval_row.get("scores") is None:
                eval_row["scores"] = {}
            for scorer in (self.scorers or []):
                scorer_name, _, _ = get_scorer_attributes(scorer)
                if scorer_name not in eval_row["scores"]:
                    eval_row["scores"][scorer_name] = {}
            print("adding row")
            print(eval_row)
            eval_rows.append(eval_row)

        # Use our plain-Python summarize (overrides Weave's)
        summary = await self.summarize(eval_rows)
        if return_rows:
            return summary, eval_rows
        return summary




    async def summarize(self, eval_rows):
        n = len(eval_rows)
        if n == 0:
            return {
                "n": 0,
                "accuracy": None,
                "exact_match": None,
                "avg_edit_distance": None,
                "avg_latency": None,
                "eval_function": {
                    "correct": {"true_count": 0, "false_count": 0, "true_fraction": None},
                    "exact_match": {"true_count": 0, "false_count": 0, "true_fraction": None},
                    "edit_distance": {"mean": None},
                },
                "model_latency": {"mean": None},
            }

        correct_true = 0
        exact_true = 0
        dists = []
        lats = []

        for r in eval_rows:
            s = (r.get("scores") or {}).get("eval_function") or {}
            if s.get("correct"):
                correct_true += 1
            if s.get("exact_match"):
                exact_true += 1
            ed = s.get("edit_distance")
            if ed is not None:
                try:
                    dists.append(float(ed))
                except Exception:
                    pass
            lat = r.get("model_latency")
            if lat is not None:
                try:
                    lats.append(float(lat))
                except Exception:
                    pass

        def mean(xs):
            return sum(xs) / len(xs) if xs else None

        acc = correct_true / n if n else None
        exm = exact_true / n if n else None
        avg_ed = mean(dists)
        avg_lat = mean(lats)

        # Return BOTH flat metrics and the nested structure expected by io.write_summary
        return {
            # flat (optional)
            "n": n,
            "accuracy": acc,
            "exact_match": exm,
            "avg_edit_distance": avg_ed,
            "avg_latency": avg_lat,
            # nested (compat with io.py)
            "eval_function": {
                "correct": {
                    "true_count": correct_true,
                    "false_count": n - correct_true,
                    "true_fraction": acc,
                },
                "exact_match": {
                    "true_count": exact_true,
                    "false_count": n - exact_true,
                    "true_fraction": exm,
                },
                "edit_distance": {"mean": avg_ed},
            },
            "model_latency": {"mean": avg_lat},
        }

