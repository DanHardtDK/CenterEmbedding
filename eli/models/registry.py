from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline


MODEL_REGISTRY = {
    "gpt-3.5-turbo": {
        "class": ChatOpenAI,
        "chat": True,
    },
    "gpt-4": {
        "class": ChatOpenAI,
        "chat": True,
    },
    "gpt-neo": {
        "class": HuggingFacePipeline,
        "chat": False,
    },
    "llama-7b-chat": {
#       "class": LlamaAPI,
        "class": OpenAI,
        "chat": True,
    },
}
