# garnish

A Python library providing decorative food embellishments — featuring recipes,
preparation techniques, and plating guidelines for culinary garnishes.

## Installation

```bash
pip install -e ".[dev]"   # development install with test dependencies
```

## Quick Start

```python
import garnish

# --- Recipes ---
recipes = garnish.all_recipes()
print(len(recipes), "garnish recipes available")

citrus = garnish.get_recipe("Citrus Twist")
print(citrus.summary())

easy_recipes = garnish.recipes_by_difficulty(garnish.DifficultyLevel.EASY)
dessert_recipes = garnish.recipes_by_tag("dessert")
quick_recipes = garnish.recipes_by_max_time(10)   # ≤ 10 minutes prep

# --- Preparation Techniques ---
techniques = garnish.all_techniques()
chiffonade = garnish.get_technique("Chiffonade")
print(chiffonade.summary())

carrot_techniques = garnish.techniques_for_ingredient("carrot")
advanced_techniques = garnish.techniques_by_difficulty(garnish.DifficultyLevel.ADVANCED)

# --- Plating Guides ---
guides = garnish.all_guides()
salmon_guide = garnish.get_guide("Pan-Seared Salmon Fillet")
print(salmon_guide.summary())

top_zone_guides = garnish.guides_by_zone(garnish.PlatingZone.TOP)
citrus_guides = garnish.guides_by_garnish("Citrus Twist")
```

## Structure

| Module | Contents |
|---|---|
| `garnish/models.py` | Data classes: `Recipe`, `Technique`, `PlatingGuide`, `Ingredient`, `PlatingElement`, `DifficultyLevel`, `PlatingZone` |
| `garnish/recipes.py` | 10 garnish recipes with lookup and filter functions |
| `garnish/techniques.py` | 8 preparation techniques with lookup and filter functions |
| `garnish/plating.py` | 5 plating guides with lookup and filter functions |

## Running Tests

```bash
pytest
```
