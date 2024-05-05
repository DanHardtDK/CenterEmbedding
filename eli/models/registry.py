
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

from eli.models.llama import Llama


MODEL_REGISTRY = {
    "gpt-3.5-turbo": ChatOpenAI,
    "gpt-4": ChatOpenAI,
    "gpt-neo": HuggingFacePipeline,
    "llama-7b-chat": Llama
}
