---
name: bmi
description: Calculate Body Mass Index (BMI) from weight and height, in metric or imperial units, and return the result with its WHO health category.
---

# BMI Skill

## Purpose
Calculates Body Mass Index (BMI) given a person's weight and height, and
classifies the result into a standard health category (Underweight, Normal
weight, Overweight, Obese).

## Inputs
| Parameter | Type  | Required | Description                                              |
|-----------|-------|----------|------------------------------------------------------------|
| weight    | float | yes      | Weight in kg (metric) or lbs (imperial). Must be > 0.       |
| height    | float | yes      | Height in meters (metric) or inches (imperial). Must be > 0.|
| unit      | str   | no       | `"metric"` (default) or `"imperial"`.                       |

## Output
A dict:
```json
{
  "bmi": 22.86,
  "category": "Normal weight"
}
```

## Formula
- Metric:   `bmi = weight(kg) / height(m)^2`
- Imperial: `bmi = weight(lbs) / height(in)^2 * 703`

## Category thresholds (WHO)
- `< 18.5`      → Underweight
- `18.5 - 24.9` → Normal weight
- `25 - 29.9`   → Overweight
- `>= 30`       → Obese

## Errors
Raises `ValueError` if:
- `weight` or `height` is <= 0
- `unit` is not `"metric"` or `"imperial"`

## Files
- `skill.py` — contains the `BMISkill` class implementing `execute(weight, height, unit="metric")`.
