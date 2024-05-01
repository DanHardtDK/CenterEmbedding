from typing import Type
from langchain.schema.language_model import BaseLanguageModel
from langchain.schema.prompt_template import BasePromptTemplate

from config import MODEL, COT_STRATEGY, API_KEY
from templates import build_template
import models as m


def build_api_handler(model: str, cot_strategy: str) -> m.APIHandler:
    """Function to build the API handler from
    the specified model. The strategy is used to
     determine the system prompt."""

    modeL_specs: dict = m.MODEL_REGISTRY[model]
    template: Type[BasePromptTemplate] = build_template(
        chat=modeL_specs["chat"],  # whether the model is a chat model
        cot_strategy=cot_strategy,
    )

    model: Type[BaseLanguageModel] = modeL_specs["class"](
        model=model, openai_api_key=API_KEY, **m.PARAMETERS
    )

    return m.APIHandler(
        model=model,
        template=template,
    )


API: Type[m.APIHandler] = build_api_handler(
    model=MODEL,
    cot_strategy=COT_STRATEGY,
)
