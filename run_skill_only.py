"""
main.py

Directly invokes the "bmi" skill (skills/bmi/skill.py) — no agent, no
routing, no LLM involved. This just proves the skill works as a standalone,
importable unit.
"""

from skills.bmi import BMISkill

def get_float(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== BMI Calculator (via skills/bmi) ===")

    unit = ""
    while unit not in ("metric", "imperial"):
        unit = input("Choose unit system (metric/imperial): ").strip().lower()
        if unit not in ("metric", "imperial"):
            print("Please type 'metric' or 'imperial'.")

    if unit == "metric":
        weight = get_float("Enter weight in kg: ")
        height = get_float("Enter height in meters (e.g. 1.75): ")
    else:
        weight = get_float("Enter weight in lbs: ")
        height = get_float("Enter height in inches: ")

    skill = BMISkill()
    try:
        result = skill.execute(weight, height, unit=unit)
        print(f"\nYour BMI is {result['bmi']} ({result['category']})")
    except ValueError as e:
        print(f"Value error: {e}")

if __name__ == "__main__":
    main()
