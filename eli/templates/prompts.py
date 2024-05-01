######################
# COT PROMPT TEMPLATES
######################


SUPERVISED_COT_TEMPLATE = """The following examples consist of a Context and a Question. 
You should give the following outputs:

A1: the Context, with a verb phrase ellipsis occurrence surrounded by *'s. 
A2: the same as A1, but now with the corresponding antecedent surrounded by *'s. 
A3: like A2, but now with the antecedent filled in where the verb phrase ellipsis occurred, and surrounded by *'s.
A: now give a Yes or No answer to the question.

{examples}

Now give the outputs for the following example:

Context: {context}
Question: {question}

"""

######################
# SELF-COT PROMPT TEMPLATES
######################

UNSUPERVISED_COT_TEMPLATE = """Your task is to answer a simple Yes/No question, using the context for the question.

{examples}

Now, answer the following question:

Context: {context}
Question {question}

Work through this question step by step, and then state your final answer as either Yes or No on a new line.
"""

######################
# NO COT PROMPT TEMPLATES
######################

# SET BASE INSTRUCTIONS
DEFAULT_TEMPLATE = """The following example consist of a context and a question.

{examples}

Context: {context}
Question: {question}

Now answer the question with only a Yes or No answer:

"""

######################
# CENTER EMBEDDING PROMPT TEMPLATES
######################

# SET BASE INSTRUCTIONS
CE_TEMPLATE = """You will be given an example consisting of a context and a question to answer. The answer should
always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single
word that is a verb.

Context: {context}
Question: {question}

Now answer the question:

"""
CE1_TEMPLATE = """You will be given an example consisting of a context and a question to answer. The answer should
always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single
word that is a verb. Here is a sample:

        "Context": "The student the man saw is happy",
        "Question": "Who saw who?",
        "Answer": "The man saw the student.",


Context: {context}
Question: {question}

Now answer the question:

"""
CE2_TEMPLATE = """You will be given an example consisting of a context and a question to answer. The answer should
always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single
word that is a verb. Here are two samples:

        "Context": "The student the man saw is happy",
        "Question": "Who saw who?",
        "Answer": "The man saw the student.",


        "Context": "The teacher the student the man saw hit is happy",
        "Question": "Who saw who?",
        "Answer": "The man saw the student.",


Context: {context}
Question: {question}

Now answer the question:

"""
