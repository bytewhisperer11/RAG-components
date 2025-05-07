from langchain.chat_models import ChatOpenAI
from langchain.callbacks import AsyncIteratorCallbackHandler
import asyncio

async def main():
    handler = AsyncIteratorCallbackHandler()
    model = ChatOpenAI(streaming=True, callbacks=[handler], temperature=0)
    task = asyncio.create_task(model.ainvoke("Explain event-driven architecture."))

    async for token in handler.aiter():
        print(token, end="", flush=True)

    await task

if __name__ == "__main__":
    asyncio.run(main())
