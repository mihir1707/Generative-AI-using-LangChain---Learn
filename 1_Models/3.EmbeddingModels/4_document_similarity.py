from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimension = 300,
)

documents = [
    "Rohit Sharma is a talented Indian batsman who is famous for his elegant batting and ability to score big hundreds.",
    "Sachin Tendulkar is a legendary Indian cricketer who is widely regarded as one of the greatest batsmen in the history of cricket.",
    "Virat Kohli is one of India's greatest batsmen and is known for his consistency and aggressive style of play.",
    "MS Dhoni is a legendary Indian wicketkeeper-batsman known for his calm leadership and finishing ability.",
    "Jasprit Bumrah is one of India's best fast bowlers and is famous for his accurate yorkers and unusual bowling action."
]

query = "tell me about rohit sharma"

doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

cosine_similarities = cosine_similarity([query_embedding], doc_embeddings)

print(cosine_similarities)

scores = cosine_similarities[0]

# print(sorted(list(enumerate(scores)), key=lambda x: x[1]))

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("Similarity Score is : ", score)