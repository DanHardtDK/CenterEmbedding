from typing import Type
from langchain.schema.language_model import BaseLanguageModel
from langchain.schema.prompt_template import BasePromptTemplate

from models.abstract import GenericAPI


class APIHandler(GenericAPI):

    """Abstract class to handle queries.
    Inherits from GenericAPI, which is a class that
     handles the queries themselves and is model-agnostic."""

    def __init__(
        self, model: Type[BaseLanguageModel], template: Type[BasePromptTemplate]
    ) -> None:
        """Initialize the class with the given model and
        system prompt,

        Args:
            model (Type[BaseLanguageModel]): the model to use
            template (Type[BasePromptTemplate]): the template to use
        """

        self.model = model
        self.template = template
