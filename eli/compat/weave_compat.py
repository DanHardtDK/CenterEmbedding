# eli/compat/weave_compat.py
from __future__ import annotations
import asyncio
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Dict, Iterable, List, Tuple, Union, Optional

# ----- Dataset -----
@dataclass
class Dataset:
    rows: Iterable[Dict[str, Any]]

# ----- Model base (optional) -----
class Model:
    """
    Minimal base class; your concrete models can ignore this and just be callables.
    """
    async def __call__(self, example: Dict[str, Any]) -> Any:
        return await self.predict(example)

    async def predict(self, example: Dict[str, Any]) -> Any:
        raise NotImplementedError

# ----- util.async_foreach -----
class util:
    @staticmethod
    async def async_foreach(
        sequence: Iterable[Any],
        func: Callable[[Any], Awaitable[Any]],
        max_concurrent_tasks: int = 1,
    ):
        sem = asyncio.Semaphore(max_concurrent_tasks)
        async def _runner(idx: int, item: Any):
            async with sem:
                res = await func(item)
                return idx, res

        tasks = [asyncio.create_task(_runner(i, item)) for i, item in enumerate(sequence)]
        for coro in asyncio.as_completed(tasks):
            yield await coro

# ----- scorer helpers -----
def get_scorer_attributes(scorer: Any) -> Tuple[str, Optional[Any], Optional[Any]]:
    """
    Return (scorer_name, _, _) like weave.flow.scorer.get_scorer_attributes did.
    We only use the name; the others stay None.
    """
    name = getattr(scorer, "name", None)
    if not name:
        name = getattr(scorer, "__name__", scorer.__class__.__name__)
    return name, None, None

# ----- Evaluation & predict_and_score -----
class Evaluation:
    """
    A tiny stand-in for weave.Evaluation, just enough for your Evaluator.
    Expected attributes (set by your code or subclass):
      - self.dataset: Dataset
      - self.scorers: Optional[List[Callable]]  (each scorer(example, model_output) -> dict)
      - self.trials: int
    """

    dataset: Dataset
    scorers: Optional[List[Callable]]
    trials: int = 1

    async def _call_model(self, model: Union[Callable, Model], example: Dict[str, Any]) -> Any:
        # Support async/sync callables and objects with predict/.__call__
        if hasattr(model, "predict"):
            out = model.predict(example)
            return await out if asyncio.iscoroutine(out) else out
        elif callable(model):
            out = model(example)
            return await out if asyncio.iscoroutine(out) else out
        raise TypeError("model must be a callable or have a .predict method")

    async def predict_and_score(self, model: Union[Callable, Model], example: Dict[str, Any]) -> Dict[str, Any]:
        model_output = await self._call_model(model, example)
        scores: Dict[str, Any] = {}

        if self.scorers:
            for scorer in self.scorers:
                scorer_name, _, _ = get_scorer_attributes(scorer)
                # Allow scorer(example, model_output) or scorer(model_output, example)
                try:
                    s = scorer(example, model_output)  # type: ignore
                except TypeError:
                    s = scorer(model_output, example)  # type: ignore
                # Normalise: if scorer returns a flat dict, tuck it under its name
                if isinstance(s, dict) and scorer_name not in s:
                    scores[scorer_name] = s
                else:
                    # Already namespaced or non-dict; keep as-is
                    scores[scorer_name] = s
        return {
            "model_output": model_output,
            "scores": scores,
            # Let callers fill latency if they want; we don’t measure here
            "model_latency": None,
        }
