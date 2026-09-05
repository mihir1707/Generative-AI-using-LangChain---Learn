# system messages
# human messages -> user send to ai which messages are human messages
# ai messages -> ai tell you answer of user query which messages are ai messages

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content='You are a helpful assistant.'),
    HumanMessage(content='Tell me about LangChain.'),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)