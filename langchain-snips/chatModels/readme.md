# 🧠 LangChain v0.3 - Top 5 Chat Model Wrappers

This repository provides **minimalist, standalone scripts** for interfacing with the top 5 enterprise-grade chat models using **LangChain v0.3**. Each script avoids chains, templates, or agents — just raw prompt-in/prompt-out via LangChain’s chat model interface.

---

## 📁 Files Overview

| File                  | Model                       | Provider         | LangChain Interface        |
|-----------------------|-----------------------------|------------------|-----------------------------|
| `1_chat_openai.py`    | GPT-4 / GPT-3.5              | OpenAI           | `ChatOpenAI`               |
| `2_chat_claude.py`    | Claude 3 (Opus/Sonnet/etc.)  | Anthropic        | `ChatAnthropic`            |
| `3_chat_gemini.py`    | Gemini Pro                   | Google GenAI     | `ChatGoogleGenerativeAI`   |
| `4_chat_mistral.py`   | Mistral-7B Instruct          | Together AI      | `ChatTogether`             |
| `5_chat_cohere.py`    | Command-R+                   | Cohere           | `ChatCohere`               |

---

## 🔌 Interface Breakdown

Each wrapper uses LangChain’s shared **chat model interface**, structured with `SystemMessage` and `HumanMessage` to standardize prompts:

```python
from langchain_core.messages import SystemMessage, HumanMessage

llm.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is vector embedding?")
])
