# # Use a pipeline as a high-level helper
# from langchain.llms import HuggingFacePipeline
# from langchain.prompts import PromptTemplate

# from prompting.abstract_query import API
# from prompting.huggingface.parameters import PARAMETERS  # noqa: F401


# class HFQuery(API):

#     """Class to handle queries to HuggingFace API"""

#     def __init__(self, model, chat, system_prompt) -> None:
#         """Initialize the class with the given model,
#         the matching system prompt, and the correct query function

#         Args:
#             model (str): The name of the model to use
#             chat (bool): Whether the model is optimized for chat.
#                          Used to select the correct query function
#             system_prompt (str): The system prompt to use

#         https://python.langchain.com/docs/integrations/llms/huggingface_pipelines
#         """
#         super().__init__()

#         self.model = model
#         self.system_prompt = system_prompt
#         self.query_function = self.select_query_func(chat)

#         self.llm = HuggingFacePipeline.from_model_id(
#             model_id=model,
#             task="text-generation",
#             model_kwargs=PARAMETERS,
#         )

#     def prompt(self, prompt):
#         """Complete a prompt with the given model."""

#         prompt = PromptTemplate.from_template(self.system_prompt + prompt + "\n")

#         return (prompt | self.llm).invoke()

#     def prompt_chat(self, prompt):
#         """Function to call API for models
#         which have been optimized for chat"""

#         prompt = PromptTemplate.from_template(self.system_prompt + prompt + "\n")

#         return (prompt | self.llm).invoke()
