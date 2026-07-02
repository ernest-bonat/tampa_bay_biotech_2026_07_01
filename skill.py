
class BMISkill:
    """
    Skill: bmi
    Calculates Body Mass Index (BMI) and returns the value with its
    WHO health category. See SKILL.md in this folder for full details.
    """

    name = "bmi"
    description = "Calculate Body Mass Index (BMI) and return the value with its health category."

    def execute(self, weight, height, unit="metric"):
        """
        Calculate BMI.

        Args:
            weight: Weight in kg (metric) or lbs (imperial)
            height: Height in meters (metric) or inches (imperial)
            unit: "metric" or "imperial"

        Returns:
            dict with 'bmi' (float) and 'category' (str)
        """
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers")

        if unit == "imperial":
            # lbs and inches -> standard imperial BMI formula
            bmi = (weight / (height ** 2)) * 703
        elif unit == "metric":
            bmi = weight / (height ** 2)
        else:
            raise ValueError("unit must be 'metric' or 'imperial'")

        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return {"bmi": bmi, "category": category}
