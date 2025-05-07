# LangChain Callback Handlers – Execution Tracing Use Case

This project showcases all major callback handlers available directly in the `langchain` package. Each script demonstrates a different approach to interacting with or monitoring model execution in a real-time or production context.

---

## 🧠 Use Case Overview

**Goal:** Provide real-time visibility and control over LLM executions in a distributed, async, or production-grade setup:
- Stream model outputs
- Capture final results
- Integrate with logging
- Enable token-wise monitoring

Each callback serves a unique role in operationalizing LangChain usage in live systems.

---

## 🗂️ Callback Handler Scripts

| Script | Handler | Purpose |
|--------|---------|---------|
| `1_async_iterator_callback.py` | `AsyncIteratorCallbackHandler` | Streams LLM tokens asynchronously using an async iterator—ideal for async apps. |
| `2_async_final_iterator_callback.py` | `AsyncFinalIteratorCallbackHandler` | Streams tokens while also allowing final output capture after generation ends. |
| `3_final_streaming_stdout_callback.py` | `FinalStreamingStdOutCallbackHandler` | Streams tokens to stdout while printing the final result cleanly. |
| `4_logging_callback.py` | `LoggingCallbackHandler` | Logs model lifecycle events using Python logging—suitable for observability stacks. |
