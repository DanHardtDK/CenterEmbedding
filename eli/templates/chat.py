from langchain.prompts import ChatPromptTemplate


class ChatTemplate:
    """Template for chat models"""

    def __init__(self, template_string: str) -> None:
        """Initialize the class"""
        # TODO: Consider whether to split up the template string
        #  into a system prompt and a user prompt.
        self.template = ChatPromptTemplate.from_messages(
            messages=[("human", template_string)]
        )

    def format_query(self, **kwargs) -> ChatPromptTemplate:
        """Format a prompt with the given input"""
        return self.template.format_messages(**kwargs)
