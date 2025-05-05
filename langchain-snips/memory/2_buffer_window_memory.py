from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferWindowMemory(k=2)  # Keep last 2 exchanges only

chain = ConversationChain(llm=llm, memory=memory)

print(chain.run("Hi, I'm Steve."))
print(chain.run("Tell me a joke."))
print(chain.run("What’s my name?"))  # May not remember if it fell out of the window
