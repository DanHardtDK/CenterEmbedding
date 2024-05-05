from openai import AsyncOpenAI
import weave
from weave import Model


class Llama(Model):

    model_name : str
    api_key : str
    prompt_template : str

    @property
    def api(self):
        return AsyncOpenAI(
            api_key=self.api_key, 
            base_url="https://api.llama-api.com"
        )
    

    def format(self, context : str, question : str, params : dict, **kwargs) -> dict:

        prompt = self.prompt_template.format(context=context, question=question)
        return {
            "messages": [
                {"role": "user", "content": prompt},
            ],
            **params,
            **kwargs
        }

    @weave.op()
    async def predict(self, context : str, question : str, params : dict = {}, **kwargs):

        payload = self.format(context, question, params, **kwargs)

        response = await self.api.chat.completions.create(
            model=self.model_name, 
            **payload
        )
        if response is None:
            raise ValueError("No response from model")

        result = response.choices[0].message.content
        return result