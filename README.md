# LangChain Agent Demo

一个用于学习LangChain Agent开发的Python项目

本项目主要用于练习：

- ChatModel调用
- Tool工具定义
- Prompt提示词管理
- Agent构建与调用
- Service层封装
- 后续扩展RAG、Memory、LangGraph等模块

## 项目结构

```text
langchain-agent-demo/
│
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── main.py
│
├── app/
│   ├── __init__.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── llm.py
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── agent_prompt.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── calculator_tool.py
│   │   └── search_tool.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   └── basic_agent.py
│   │
│   └── services/
│       ├── __init__.py
│       └── agent_service.py
│
└── tests/
    ├── __init__.py
    └── test_agent.py