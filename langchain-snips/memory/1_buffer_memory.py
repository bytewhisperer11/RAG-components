from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory()

chain = ConversationChain(llm=llm, memory=memory)

print(chain.run("Hi, I'm Elon."))
print(chain.run("What did I say my name was?"))
