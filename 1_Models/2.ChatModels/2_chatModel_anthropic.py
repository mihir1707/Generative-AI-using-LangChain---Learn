from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3-opus-20241217', temperature=0.7, max_completion_tokens=1000)

result = model.invoke("What is the capital of India?")

print(result.content)
print(result)