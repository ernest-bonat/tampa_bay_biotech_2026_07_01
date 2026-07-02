"""
tools.py

Shared LangChain tools, built on top of skills/. Any agent can import
from here to reuse the same skill implementation instead of redefining it.
"""

from langchain_core.tools import tool

from skills.bmi import BMISkill

_bmi_skill = BMISkill()


@tool
def bmi_tool(weight: float, height: float, unit: str = "metric") -> dict:
    """Calculate Body Mass Index (BMI) and its health category.

    Args:
        weight: Weight in kg (metric) or lbs (imperial). Must be > 0.
        height: Height in meters (metric) or inches (imperial). Must be > 0.
        unit: "metric" or "imperial". Defaults to "metric".

    Returns:
        A dict like {"bmi": 22.86, "category": "Normal weight"}.
    """
    return _bmi_skill.execute(weight, height, unit=unit)
