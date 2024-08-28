#query_doc.py

from indexify import IndexifyClient
from groq import Groq


client = IndexifyClient()
groq_client = Groq(
    api_key="API_KEY",
)

def get_context(question: str, index: str, top_k=3):
    results = client.search_index(name=index, query=question, top_k=3)
    context = ""
    for result in results:
        context = context + f"content id: {result['content_id']} \n \npassage: {result['text']}\n"
    return context

def create_prompt(question, context):
    return f"You are a real estate expert. Answer the question, based on the context. Answer \"Information not found\" if there is no context. Do not hallucinate.  \nquestion: {question}  \ncontext: {context}"


def generate_response(prompt):
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gemma-7b-it",
    )
    return chat_completion.choices[0].message.content

question = "What are the risks of earthquake damage and what mitigation measures are taken?"
context = get_context(question, "pdfqa1.pdfembedding.embedding")
prompt = create_prompt(question, context)

response = generate_response(prompt)
print(response)