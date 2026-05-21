"""Garnish — culinary garnish recipes, techniques, and plating guides.

Public API
----------
Recipes::

    from garnish import all_recipes, get_recipe, recipes_by_difficulty, recipes_by_tag
    from garnish import recipes_by_max_time

Techniques::

    from garnish import all_techniques, get_technique
    from garnish import techniques_by_difficulty, techniques_for_ingredient

Plating guides::

    from garnish import all_guides, get_guide, guides_by_garnish, guides_by_zone

Models::

    from garnish.models import (
        DifficultyLevel, PlatingZone,
        Ingredient, Recipe, Technique, PlatingElement, PlatingGuide,
    )
"""

from .models import (
    DifficultyLevel,
    Ingredient,
    PlatingElement,
    PlatingGuide,
    PlatingZone,
    Recipe,
    Technique,
)
from .plating import (
    all_guides,
    get_guide,
    guides_by_garnish,
    guides_by_zone,
)
from .recipes import (
    all_recipes,
    get_recipe,
    recipes_by_difficulty,
    recipes_by_max_time,
    recipes_by_tag,
)
from .techniques import (
    all_techniques,
    get_technique,
    techniques_by_difficulty,
    techniques_for_ingredient,
)

__all__ = [
    # Models
    "DifficultyLevel",
    "PlatingZone",
    "Ingredient",
    "Recipe",
    "Technique",
    "PlatingElement",
    "PlatingGuide",
    # Recipe API
    "all_recipes",
    "get_recipe",
    "recipes_by_difficulty",
    "recipes_by_tag",
    "recipes_by_max_time",
    # Technique API
    "all_techniques",
    "get_technique",
    "techniques_by_difficulty",
    "techniques_for_ingredient",
    # Plating API
    "all_guides",
    "get_guide",
    "guides_by_garnish",
    "guides_by_zone",
]
