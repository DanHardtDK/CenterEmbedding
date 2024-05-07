import templates.center_embed as CE
from templates.default import DEFAULT_TEMPLATE
from templates.supervised_cot import SUPERVISED_COT_TEMPLATE
from templates.unsupervised_cot import UNSUPERVISED_COT_TEMPLATE

PROMPT_TEMPLATE_REGISTRY = {
    "center_embed": CE.CE_TEMPLATE,
    "center_embed_tn1": CE.CE_TEMPLATE_Tn1,
    "center_embed_tn2": CE.CE_TEMPLATE_Tn2,
    "default": DEFAULT_TEMPLATE,
    "supervised-cot": SUPERVISED_COT_TEMPLATE,
    "unsupervised-cot": UNSUPERVISED_COT_TEMPLATE,
}
