from typing import Type
from langchain.prompts import PromptTemplate


class DefaultTemplate:
    """Prompt template for default models"""

    def __init__(self, template_string: str) -> None:
        """Initialize the class"""
        self.template: Type[PromptTemplate] = PromptTemplate.from_template(
            template_string
        )

    def format_query(self, **kwargs) -> PromptTemplate:
        """Format a prompt with the given input"""
        return self.template.format(**kwargs)
