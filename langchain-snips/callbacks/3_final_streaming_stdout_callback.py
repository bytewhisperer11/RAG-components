from langchain.chat_models import ChatOpenAI
from langchain.callbacks import FinalStreamingStdOutCallbackHandler

llm = ChatOpenAI(streaming=True, callbacks=[FinalStreamingStdOutCallbackHandler()], temperature=0)
llm.invoke("Explain the CAP theorem in distributed systems.")
