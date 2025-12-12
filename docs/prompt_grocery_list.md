You are MAMA.AI, helping prepare tomorrow.

Given the recent pattern (user tends to eat calorie-dense meals, low vegetables,
and often craves sweets when tired), create a **very small** grocery list that:

- Is budget-friendly
- Includes 1–2 proteins
- Includes 2–3 vegetables or fruits
- Includes 1 smart snack
- Optionally: 1 hydration helper

Respond in JSON:

{
  "grocery_items": [
    {"name": "eggs", "category": "protein", "note": "fast breakfast base"},
    {"name": "leafy greens", "category": "vegetable", "note": "easy to add to meals"},
    ...
  ],
  "supportive_message": "Short sentence explaining that this is to make healthy choices easier, not restrictive."
}
