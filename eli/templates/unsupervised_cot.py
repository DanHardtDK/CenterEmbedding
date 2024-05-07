UNSUPERVISED_COT_TEMPLATE = """Your task is to answer a simple Yes/No question, using the context for the question.

{examples}

Now, answer the following question:

Context: {context}
Question {question}

Work through this question step by step, and then state your final answer as either Yes or No on a new line.
"""
