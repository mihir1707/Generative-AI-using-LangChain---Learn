from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Gandhinagar is the capital of Gujarat",
    "Mumbai is the capital of Maharashtra",
    "Kolkata is the capital of West Bengal",
    "Delhi is the capital of India",
]

result = embeddings.embed_documents(documents)

print(result)
print(str(result))