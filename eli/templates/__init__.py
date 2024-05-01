from typing import Callable

from templates.chat import ChatTemplate
from templates.default import DefaultTemplate
import templates.prompts as prompts


# Lookup table for the prompt template to use for each strategy
STRATEGY_PROMPT_CHOICE = {
    "supervised": prompts.SUPERVISED_COT_TEMPLATE,
    "unsupervised": prompts.UNSUPERVISED_COT_TEMPLATE,
    "default": prompts.DEFAULT_TEMPLATE,
    "centerembed": prompts.CE_TEMPLATE,
    "centerembedP1": prompts.CE1_TEMPLATE,
    "centerembedP2": prompts.CE2_TEMPLATE,
    # TODO: add more strategies
}

TEMPLATE_CHOICE = {
    True: ChatTemplate,
    False: DefaultTemplate,
}


def build_template(chat: bool, cot_strategy: str) -> Callable:
    """Build the template for the given model.
    We use the strategy to determine the system prompt.
    For example, if the strategy is CoT, we use the CoT system prompt.
    If the strategy is default, we use the default system prompt.

    The chat flag is used to determine whether the model is a chat model.
    If the model is a chat model, we use the chat template.
    If the model is not a chat model, we use the default template.

    Args:
        chat (bool): whether the model is a chat model
        strategy (str): the experiment strategy to use
    """
    prompt = STRATEGY_PROMPT_CHOICE[cot_strategy]
    return TEMPLATE_CHOICE[chat](template_string=prompt)
