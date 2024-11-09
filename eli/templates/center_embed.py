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

        Context: The teacher the student the driver the girl saw hit hates left.
        Question: Who hit who?
        Answer: the driver hit the student.

        Context: The teacher the student the driver the girl saw hit hates is glad.
        Question: Who hit who?
        Answer: the driver hit the student.

        Context: The teacher the student the driver the girl saw hit knows is happy.
        Question: Who hit who?
        Answer: the driver hit the student.

        Context: The teacher the student the driver the girl saw hit knows left.
        Question: Who hit who?
        Answer: the driver hit the student.

        Context: The teacher the student the driver the girl saw hit knows is glad.
        Question: Who hit who?
        Answer: the driver hit the student.

        Context: The teacher the student the driver the girl saw likes hit is happy.
        Question: Who likes who?
        Answer: the driver likes the student.



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

        Context: The man the woman the girl the driver the student saw hit likes knows left.
        Question: Who hit who?
        Answer: the driver hit the girl.

        Context: The woman the student the man the teacher the girl likes hit saw hates is glad.
        Question: Who hit who?
        Answer: the teacher hit the man.

        Context: The boy the driver the student the man the woman hates hit saw knows is happy.
        Question: Who hit who?
        Answer: the man hit the student.

        Context: The driver the man the teacher the student the woman hates likes knows saw left.
        Question: Who likes who?
        Answer: the student likes the teacher.

        Context: The boy the girl the man the teacher the student hit likes hates knows left.
        Question: Who likes who?
        Answer: the teacher likes the man.

        Context: The student the girl the man the driver the teacher likes hates hit knows is happy.
        Question: Who hates who?
        Answer: the driver hates the man.



Now answer the question:

Context: {context}
Question: {question}
"""








        # Context: The girl the student the teacher the driver the man saw hates hit likes left.
        # Question: Who hates who?
        # Answer: the driver hates the teacher.

        # Context: The woman the boy the man the driver the student saw hit hates likes is glad.
        # Question: Who hit who?
        # Answer: the driver hit the man.

        # Context: The student the woman the girl the teacher the boy hates saw likes hit left.
        # Question: Who saw who?
        # Answer: the teacher saw the girl.

        # Context: The driver the woman the student the boy the teacher likes knows hit saw is happy.
        # Question: Who knows who?
        # Answer: the boy knows the student.

        # Context: The man the woman the girl the driver the student saw hit likes knows left.
        # Question: Who hit who?
        # Answer: the driver hit the girl.

        # Context: The woman the student the man the teacher the girl likes hit saw hates is glad.
        # Question: Who hit who?
        # Answer: the teacher hit the man.

        # Context: The boy the driver the student the man the woman hates hit saw knows is happy.
        # Question: Who hit who?
        # Answer: the man hit the student.

        # Context: The driver the man the teacher the student the woman hates likes knows saw left.
        # Question: Who likes who?
        # Answer: the student likes the teacher.

        # Context: The boy the girl the man the teacher the student hit likes hates knows left.
        # Question: Who likes who?
        # Answer: the teacher likes the man.

        # Context: The student the girl the man the driver the teacher likes hates hit knows is happy.
        # Question: Who hates who?
        # Answer: the driver hates the man.

        # Context: The boy the girl the man the student the driver likes knows saw hit is glad.
        # Question: Who knows who?
        # Answer: the student knows the man.

        # Context: The driver the woman the boy the girl the teacher saw likes knows hates left.
        # Question: Who likes who?
        # Answer: the girl likes the boy.

        # Context: The man the driver the girl the teacher the woman hit saw hates knows is glad.
        # Question: Who saw who?
        # Answer: the teacher saw the girl.

        # Context: The driver the girl the man the student the boy hit likes hates knows left.
        # Question: Who likes who?
        # Answer: the student likes the man.

        # Context: The woman the man the girl the driver the teacher saw hates knows hit is glad.
        # Question: Who hates who?
        # Answer: the driver hates the girl.

        # Context: The teacher the woman the driver the student the man hit hates knows likes left.
        # Question: Who hates who?
        # Answer: the student hates the driver.

        # Context: The student the woman the man the driver the girl likes knows hates saw is glad.
        # Question: Who knows who?
        # Answer: the driver knows the man.

        # Context: The woman the boy the student the girl the driver knows hates likes hit left.
        # Question: Who hates who?
        # Answer: the girl hates the student.

        # Context: The student the girl the teacher the man the boy saw knows hates hit left.
        # Question: Who knows who?
        # Answer: the man knows the teacher.

        # Context: The man the driver the woman the student the girl hates knows likes hit is glad.
        # Question: Who knows who?
        # Answer: the student knows the woman.




        # Context: The teacher the student the driver the girl saw hit likes is happy.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit likes left.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit likes is glad.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit hates is happy.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit hates left.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit hates is glad.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit knows is happy.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit knows left.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw hit knows is glad.
        # Question: Who hit who?
        # Answer: the driver hit the student.

        # Context: The teacher the student the driver the girl saw likes hit is happy.
        # Question: Who likes who?
        # Answer: the driver likes the student.

        
