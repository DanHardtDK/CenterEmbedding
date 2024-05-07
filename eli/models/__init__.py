
from models.llama import Llama
from models.openai import OpenAI


MODEL_REGISTRY = {
    "gpt-3.5-turbo": OpenAI,
    "gpt-4": OpenAI,
    "llama-7b-chat": Llama
}

