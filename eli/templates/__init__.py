import templates.center_embed as CE
from templates.default import DEFAULT_TEMPLATE
from templates.supervised_cot import SUPERVISED_COT_TEMPLATE
from templates.unsupervised_cot import UNSUPERVISED_COT_TEMPLATE

PROMPT_TEMPLATE_REGISTRY = {
    "center_embed": CE.CE_TEMPLATE,
    "center_embed_tn1": CE.CE_TEMPLATE_Tn1,
    "center_embed_tn2": CE.CE_TEMPLATE_Tn2,
    "center_embed_tn2_2": CE.CE_TEMPLATE_Tn2_2,    
    "center_embed_tn3": CE.CE_TEMPLATE_Tn3,
    "center_embed_tn3_2": CE.CE_TEMPLATE_Tn3_2,
    "center_embed_tn3_only": CE.CE_TEMPLATE_Tn3_ONLY,    
    "center_embed_tn4": CE.CE_TEMPLATE_Tn4,
    "center_embed_tn4_2": CE.CE_TEMPLATE_Tn4_2,
    "center_embed_tn4_only": CE.CE_TEMPLATE_Tn4_ONLY,                    
    "default": DEFAULT_TEMPLATE,
    "supervised-cot": SUPERVISED_COT_TEMPLATE,
    "unsupervised-cot": UNSUPERVISED_COT_TEMPLATE,
}
