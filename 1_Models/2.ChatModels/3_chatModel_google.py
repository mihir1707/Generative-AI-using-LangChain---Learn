from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.7, max_completion_tokens=1000)

result = model.invoke("What is the capital of India?")

print(result.content)
print(result)