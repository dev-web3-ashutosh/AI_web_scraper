from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key="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",
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

response=llm.invoke("Who was the first person to walk on moon?")
print(response.content)