"""
fitness_coach_agent.py

A SECOND agent, separate from agent.py, that reuses the exact same
bmi_tool (from tools.py -> skills/bmi/skill.py). This demonstrates that a
skill is a reusable unit of capability, not something tied to one agent.

Where agent.py is a plain "BMI calculator" persona, this agent is a
"Fitness Coach" persona: it still calls bmi_tool to get the number, but
wraps it with exercise guidance tailored to the resulting category.
"""

import os

from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent

from tools import bmi_tool

SYSTEM_PROMPT = (
    "You are a supportive, certified fitness coach. "
    "Always use the `bmi_tool` to calculate BMI before giving advice — "
    "never estimate it yourself. Based on the resulting category, give "
    "a short, practical exercise recommendation:\n"
    "- Underweight: focus on strength training and a calorie surplus.\n"
    "- Normal weight: general maintenance — mix of cardio and strength.\n"
    "- Overweight: gradual cardio increase plus strength training, "
    "sustainable pace.\n"
    "- Obese: low-impact cardio (walking, swimming) and consulting a "
    "doctor before starting a new program.\n"
    "Keep tone encouraging, not judgmental. Always include a brief note "
    "that this is general guidance, not medical advice, and a doctor "
    "should be consulted for a personalized plan."
)


def build_model():
    """Creates the LLM used to power the agent. Requires OPENAI_API_KEY."""
    if not os.environ.get("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Copy .env.example to .env and "
            "add your key, or export it in your shell."
        )
    model_name = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
    return ChatOpenAI(model=model_name, temperature=0)


def build_agent(model=None):
    """Builds the compiled LangGraph fitness-coach agent with bmi_tool attached."""
    model = model or build_model()
    return create_agent(
        model,
        tools=[bmi_tool],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver(),
    )
