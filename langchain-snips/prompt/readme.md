# LangChain Prompt Interfaces – Project Creation Use Case

This project demonstrates all major LangChain prompt interfaces, each implemented in a separate Python script. The use case is centered on **automated project design**, where the AI acts as a senior software architect creating technical scaffolding from natural language instructions.

---

## 🧠 Use Case Overview

**Goal:** Automatically generate a full-stack project blueprint based on user-provided input:
- Project Title
- Purpose/Goal
- Tech Stack
- Features
- Constraints

Each prompt interface serves a unique role in modeling or interacting with LLMs for this automation workflow.

---

## 🗂️ Prompt Interface Scripts

| Script | Interface | Purpose |
|--------|-----------|---------|
| `1_prompt_template.py` | `PromptTemplate` | Simple one-turn prompt for generating a complete project plan from static inputs. |
| `2_few_shot_prompt.py` | `FewShotPromptTemplate` | Provides multiple example outputs to guide the LLM in generating new similar project blueprints. |
| `3_chat_prompt.py` | `ChatPromptTemplate` + `MessagesPlaceholder` | Simulates a multi-turn dialog between the user and an AI architect with memory of prior turns. |
| `4_system_prompt.py` | `SystemMessagePromptTemplate` | Configures the AI’s role (system persona) as a software architect. |
| `5_ai_prompt.py` | `AIMessagePromptTemplate` | Models AI's expected or intermediate response formatting. |
| `6_messages_placeholder.py` | `MessagesPlaceholder` | Enables injection of prior conversation history into a prompt chain. |

<img src="sequence.svg" alt="LangChain Agent Flowchart" alt="Agent Flow" width="1200" height="800" />


