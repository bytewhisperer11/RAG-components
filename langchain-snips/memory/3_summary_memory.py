from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory

llm = ChatOpenAI(temperature=0)

memory = ConversationSummaryMemory(llm=llm)

chain = ConversationChain(llm=llm, memory=memory)

print(chain.run("Hi, I'm Jane. I work at SpaceX."))
print(chain.run("Tell me something interesting about rockets."))
print(chain.run("What do you remember about me?"))
