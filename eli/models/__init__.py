# TODO: Create classes for all the providers
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline

from models.llama import Llama


MODEL_REGISTRY = {
    "gpt-3.5-turbo": ChatOpenAI,
    "gpt-4": ChatOpenAI,
    "gpt-neo": HuggingFacePipeline,
    "llama-7b-chat": Llama
}

