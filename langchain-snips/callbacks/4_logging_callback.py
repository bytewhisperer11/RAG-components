import logging
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import LoggingCallbackHandler

logging.basicConfig(level=logging.INFO)

llm = ChatOpenAI(callbacks=[LoggingCallbackHandler()], temperature=0)
llm.invoke("What is the role of a service mesh in microservice architecture?")
