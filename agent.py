"""
agent.py

Wraps the "bmi" skill (skills/bmi/skill.py) as a LangGraph tool-calling
agent, so a user can ask in natural language ("I'm 70kg and 1.75m tall,
what's my BMI?") and the agent decides when/how to call the skill.

Framework notes:
- Uses LangGraph's `create_agent` (the current, non-deprecated API in
  LangGraph 1.x; it replaces the old `create_react_agent`).
- Google ADK is NOT used here. For a single-skill, single-tool agent like
  this, LangGraph's built-in ReAct-style agent is sufficient — ADK's extra
  orchestration (multi-agent hierarchies, session/state services, etc.)
  isn't needed. If this project grows into multiple cooperating agents,
  ADK becomes worth reconsidering.
"""

import os

from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()

from tools import bmi_tool

SYSTEM_PROMPT = (
    "You are a helpful health-metrics assistant. "
    "You have access to a `bmi_tool` that calculates BMI. "
    "Always use the tool to compute BMI rather than doing the math yourself. "
    "If the user doesn't specify units, ask them or assume metric (kg/m) "
    "and say so. Clearly state the BMI value and category in your answer."
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
    """Builds the compiled LangGraph agent with the bmi_tool attached."""
    model = model or build_model()
    return create_agent(
        model,
        tools=[bmi_tool],
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver(),
    )
