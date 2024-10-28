######################
# CENTER EMBEDDING PROMPT TEMPLATES
######################

# SET BASE INSTRUCTIONS
CE_TEMPLATE = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N, where N stands for a single word that is a noun, and V stands for a single word that is a verb.

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
Question: Who hit who?
Answer: The student hit the teacher.

Now answer the question:

Context: {context}
Question: {question}
"""

CE_TEMPLATE_Tn2_2 = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are two samples:

Context: The student the man saw is happy.
Question: Who saw who?
Answer: The man saw the student.

Context: The man the student saw is happy.
Question: Who saw who?
Answer: The student saw the man.


Context: The teacher the student the man saw hit is happy.
Question: Who hit who?
Answer: The student hit the teacher.


Context: The student the teacher the man saw hit is happy.
Question: Who hit who?
Answer: The teacher hit the student.

Now answer the question:

Context: {context}
Question: {question}
"""


CE_TEMPLATE_Tn3 = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are three samples:

Context: The student the man saw is happy.
Question: Who saw who?
Answer: The man saw the student.

Context: The teacher the student the man saw hit is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Context: The lady the teacher the student the man saw hit likes is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Now answer the question:

Context: {context}
Question: {question}
"""

CE_TEMPLATE_Tn3_2 = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are three samples:

Context: The student the man saw is happy.
Question: Who saw who?
Answer: The man saw the student.

Context: The man the student saw is happy.
Question: Who saw who?
Answer: The student saw the man.


Context: The teacher the student the man saw hit is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Context: The student the teacher the man saw hit is happy.
Question: Who hit who?
Answer: The teacher hit the student.


Context: The lady the teacher the student the man saw hit likes is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Context: The lady the student the teacher the man saw hit likes is happy.
Question: Who hit who?
Answer: The teacher hit the student.

Now answer the question:

Context: {context}
Question: {question}
"""
CE_TEMPLATE_Tn3_ONLY = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are samples:


Context: The teacher the student the driver the girl saw hit likes is happy.
Question: Who hit who?
Answer: the driver hit the student.

Context: The teacher the student the driver the girl saw hit likes left.
Question: Who hit who?
Answer: the driver hit the student.

Context: The teacher the student the driver the girl saw hit likes is glad.
Question: Who hit who?
Answer: the driver hit the student.

Context: The teacher the student the driver the girl saw hit hates is happy.
Question: Who hit who?
Answer: the driver hit the student.


Now answer the question:

Context: {context}
Question: {question}
"""








CE_TEMPLATE_Tn4 = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are samples:

Context: The student the man saw is happy.
Question: Who saw who?
Answer: The man saw the student.


Context: The teacher the student the man saw hit is happy.
Question: Who hit who?
Answer: The student hit the teacher.


Context: The lady the teacher the student the man saw hit likes is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Context: The driver the lady the teacher the student the man saw hit likes helped is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Now answer the question:

Context: {context}
Question: {question}
"""

CE_TEMPLATE_Tn4_2 = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are samples:

Context: The student the man saw is happy.
Question: Who saw who?
Answer: The man saw the student.

Context: The man the student saw is happy.
Question: Who saw who?
Answer: The student saw the man.


Context: The teacher the student the man saw hit is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Context: The student the teacher the man saw hit is happy.
Question: Who hit who?
Answer: The teacher hit the student.


Context: The lady the teacher the student the man saw hit likes is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Context: The lady the student the teacher the man saw hit likes is happy.
Question: Who hit who?
Answer: The teacher hit the student.


Context: The driver the lady the teacher the student the man saw hit likes helped is happy.
Question: Who hit who?
Answer: The student hit the teacher.

Context: The driver the lady the student the teacher the man saw hit likes helped is happy.
Question: Who hit who?
Answer: The teacher hit the student.

Now answer the question:

Context: {context}
Question: {question}
"""



CE_TEMPLATE_Tn4_ONLY = """You will be given an example consisting of a context and a question to answer. The answer should always be of this form "The N V the N", where N stands for a single word that is a noun, and V stands for a single word that is a verb. Here are samples:


Context: The girl the student the teacher the driver the man saw hates hit likes left.
Question: Who hates who?
Answer: the driver hates the teacher.

Context: The woman the boy the man the driver the student saw hit hates likes is glad.
Question: Who hit who?
Answer: the driver hit the man.

Context: The student the woman the girl the teacher the boy hates saw likes hit left.
Question: Who saw who?
Answer: the teacher saw the girl.

Context: The driver the woman the student the boy the teacher likes knows hit saw is happy.
Question: Who knows who?
Answer: the boy knows the student.

Now answer the question:

Context: {context}
Question: {question}
"""




        

