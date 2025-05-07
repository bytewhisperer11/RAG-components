from langchain.chat_models import ChatOpenAI
from langchain.callbacks import AsyncFinalIteratorCallbackHandler
import asyncio

async def main():
    handler = AsyncFinalIteratorCallbackHandler()
    model = ChatOpenAI(streaming=True, callbacks=[handler], temperature=0)
    task = asyncio.create_task(model.ainvoke("List 5 benefits of microservices."))

    async for token in handler.aiter():
        print(token, end="", flush=True)

    final_output = await handler.final_output()
    print("\n\nFinal Output:", final_output)
    await task

if __name__ == "__main__":
    asyncio.run(main())
