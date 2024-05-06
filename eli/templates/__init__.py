from templates.center_embed import CE_TEMPLATE
from templates.default import DEFAULT_TEMPLATE
from templates.supervised_cot import SUPERVISED_COT_TEMPLATE
from templates.unsupervised_cot import UNSUPERVISED_COT_TEMPLATE

PROMPT_TEMPLATE_REGISTRY = {
    "center_embed": CE_TEMPLATE,
    "default": DEFAULT_TEMPLATE,
    "supervised-cot": SUPERVISED_COT_TEMPLATE,
    "unsupervised-cot": UNSUPERVISED_COT_TEMPLATE
}