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
