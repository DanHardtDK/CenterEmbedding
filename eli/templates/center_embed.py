######################
# CENTER EMBEDDING PROMPT TEMPLATES
######################

# SET BASE INSTRUCTIONS
CE_TEMPLATE = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb.

Now answer the question:

Context: {context}
Question: {question}
"""

CE_TEMPLATE_Tn1 = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. 
Here is an example:

Context: The student the man saw is happy.
Question: Who saw who?
Answer: The man saw the student.

Now answer the question:

Context: {context}
Question: {question}
"""

CE_TEMPLATE_Tn2 = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are two samples:

Context: The student the man saw is happy.
Question: Who saw who?
Answer: The man saw the student.

Context: The teacher the student the man saw hit is happy.
Question: Who saw who?
Answer: The man saw the student.

Now answer the question:

Context: {context}
Question: {question}
"""
