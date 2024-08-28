# langchain_query_doc.py

import requests
import dotenv


# Setup retreiver
from indexify import IndexifyClient
from indexify_langchain import IndexifyRetriever
client = IndexifyClient()
params = {"name": "pdfqa1.pdfembedding.embedding", "top_k": 2}
retriever = IndexifyRetriever(client=client, params=params)

from langchain_groq import ChatGroq
llm = ChatGroq(
    model="gemma-7b-it",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="API_KEY",
)

# Setup Chat Prompt Template
from langchain.prompts import ChatPromptTemplate

template = """
You are a real estate expert. Answer the question, based on the context. Answer \"Information not found\" if there is no context. 
Do not hallucinate.  \nquestion: {question}  \ncontext: {context}
"""
prompt = ChatPromptTemplate.from_template(template)

from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Query

query = "What are the risks of earthquake damage and what mitigation measures are taken?"
print(rag_chain.invoke(query))
