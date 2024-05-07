from openai import AsyncOpenAI
import weave
from weave import Model

from utils.args import CONFIG


class Llama(Model):

    model_name : str
    prompt_template : str

    @property
    def api_key(self):
        if api_key := CONFIG.get("DEFAULT", "LLAMA_KEY"):
            return api_key
        raise ValueError("LLAMA API_KEY not set in config.cfg")

    @property
    def api(self):
        # since weave evaluation is an async function, 
        # we need to use the async version of the OpenAI API
        return AsyncOpenAI(
            api_key=self.api_key, 
            base_url="https://api.llama-api.com"
        )
    
    def format(self, context : str, question : str, params : dict) -> dict:
        prompt = self.prompt_template.format(context=context, question=question)
        return {
            "messages": [
                {"role": "user", "content": prompt},
            ],
            **params,
        }

    @weave.op()
    async def predict(
        self,
        context : str,
        question : str,
        params : dict = {},
        **kwargs
    ):

        # format the payload
        payload = self.format(context, question, params)

        # make the request
        response = await self.api.chat.completions.create(
            model=self.model_name, 
            **payload
        )
        if response is None:
            raise ValueError("No response from model")

        # unpack the response
        result = response.choices[0].message.content
        return result