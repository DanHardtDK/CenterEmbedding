from langchain.chat_models.openai import ChatOpenAI
from langchain.llms import OpenAI
from llamaapi import LlamaAPI
from langchain.llms import HuggingFacePipeline


MODEL_REGISTRY = {
    "gpt-3.5-turbo": {
        "class": ChatOpenAI,
        "chat": True,
    },
    "gpt-4": {
        "class": ChatOpenAI,
        "chat": True,
    },
    "text-davinci-003": {
        "class": OpenAI,
        "chat": False,
    },
    "text-davinci-002": {
        "class": OpenAI,
        "chat": False,
    },
    "text-ada-001": {
        "class": OpenAI,
        "chat": False,
    },
    "text-curie-001": {
        "class": OpenAI,
        "chat": False,
    },
    "text-babbage-001": {
        "class": OpenAI,
        "chat": False,
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
