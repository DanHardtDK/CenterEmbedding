from eli.models.abstract import GenericAPI

from openai import OpenAI
from config import LLAMA_KEY


class Llama(GenericAPI):

    def __init__(self, model, params) -> None:
        
        self.params : dict = params
        self.model : str = model
        self.model = OpenAI(
            api_key=LLAMA_KEY, 
            base_url="https://api.llama-api.com"
        )

    def preprocess(self, payload) -> str:
        return {
            "messages": [
                {"role": "user", "content": payload},
            ],
            **self.params
        }

    def predict(self, prompt: dict) -> str:
        return self.model.chat.completions.create(
            model=self.model, 
            **prompt
        )

    def postprocess(self, prediction: str) -> str:
        # Example postprocessing: convert prediction to uppercase
        return prediction["choices"][0]["message"]["content"]
