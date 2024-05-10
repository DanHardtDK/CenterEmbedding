from models.llama import Llama
from models.openai import OpenAI


MODEL_REGISTRY = {
    "gpt-3.5-turbo": OpenAI,
    "gpt-4": OpenAI,
    "llama-7b-chat": Llama,
    "llama3-8b": Llama,
    "llama3-70b": Llama,
    "alpaca-7b": Llama,
    "vicuna-7b": Llama,
    "vicuna-13b": Llama,
    "vicuna-13b-16k": Llama,
    "falcon-7b-instruct": Llama,
    "falcon-40b-instruct": Llama,
    "openassistant-llama2-70b": Llama,
    "Nous-Hermes-Llama2-13b": Llama,
    "Nous-Hermes-llama-2-7b": Llama,
    "Nous-Hermes-2-Mistral-7B-DPO": Llama,
    "Nous-Hermes-2-Mixtral-8x7B-SFT": Llama,
    "Nous-Hermes-2-Mixtral-8x7B-DPO": Llama,
    "Nous-Hermes-2-Yi-34B": Llama,
    "Nous-Capybara-7B-V1p9": Llama,
    "OpenHermes-2p5-Mistral-7B": Llama,
    "OpenHermes-2-Mistral-7B": Llama,
    "Qwen1.5-72B-Chat": Llama,  # ( replace 72B with 32B / 14B / 7B / 4B / 1.8B / 0.5B)
}
