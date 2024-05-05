from openai import OpenAI
import weave
from weave import Model
from pydantic import field_validator


class Llama(Model):

    model_name : str
    api_key : str
    prompt : str

    @property
    def api(self):
        return OpenAI(
            api_key=self.api_key, 
            base_url="https://api.llama-api.com"
        )
    

    def preprocess(self, params : dict, **kwargs) -> dict:
        return {
            "messages": [
                {"role": "user", "content": self.prompt},
            ],
            **params,
            **kwargs
        }

    @weave.op()
    async def predict(self, prompt: str, params : dict, **kwargs):
        response = await self.api.chat.completions.create(
            model=self.model_name, 
            **self.preprocess(prompt, params, **kwargs)
        )
        result = response.choices[0].message.content

        if result is None:
            raise ValueError("No response from model")
        parsed = json.loads(result)
        return parsed