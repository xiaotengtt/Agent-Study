import os

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="qwen3.6-plus",
    api_key=os.getenv("ANTHROPIC_API_KEY"), #"sk-b5cc3c2e99f14dd0b8427995f903ea7e"
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)



@tool
def multiply(a: int, b: int) -> int:
    """计算两个整数的乘积"""
    return a * b

agent = create_agent(
    model=llm,
    tools=[multiply],
)

result = agent.invoke({
    "messages": [
        HumanMessage(content="请帮我计算 123 * 456")
    ]
})

print(result)