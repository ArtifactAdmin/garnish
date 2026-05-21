"""Culinary garnish recipes: definitions and lookup utilities."""

from __future__ import annotations

from typing import Dict, List, Optional

from .models import DifficultyLevel, Ingredient, Recipe

# ---------------------------------------------------------------------------
# Recipe catalogue
# ---------------------------------------------------------------------------

_RECIPES: List[Recipe] = [
    Recipe(
        name="Citrus Twist",
        description=(
            "A thin spiral of citrus peel that adds bright colour and aroma "
            "to cocktails, desserts, and savoury dishes."
        ),
        ingredients=[
            Ingredient("lemon, lime, or orange", "1 whole", "unwaxed skin preferred"),
        ],
        steps=[
            "Wash and dry the citrus fruit thoroughly.",
            "Use a channel knife or vegetable peeler to cut a long, thin strip "
            "of peel, following the curve of the fruit.",
            "Wrap the strip tightly around a chopstick or skewer and hold for "
            "30 seconds to set the curl.",
            "Slide off the skewer and refrigerate on a damp paper towel until "
            "ready to use.",
        ],
        difficulty=DifficultyLevel.EASY,
        prep_time_minutes=5,
        tags=["citrus", "cocktail", "dessert", "no-cook"],
        yield_description="6–8 twists per fruit",
    ),
    Recipe(
        name="Herb Chiffonade",
        description=(
            "Fine ribbon-like strips of fresh basil or mint that make a "
            "fragrant, vibrant topping for soups, salads, and pastas."
        ),
        ingredients=[
            Ingredient("fresh basil or mint leaves", "20 large leaves", "stems removed"),
        ],
        steps=[
            "Stack the leaves on top of one another, largest leaf on the bottom.",
            "Roll the stack tightly into a cigar shape.",
            "Use a sharp chef's knife to slice across the roll in thin strips "
            "(about 1–2 mm wide).",
            "Gently shake the strips apart and use immediately to preserve colour.",
        ],
        difficulty=DifficultyLevel.EASY,
        prep_time_minutes=3,
        tags=["herb", "basil", "mint", "knife-skill", "no-cook"],
        yield_description="small handful of ribbons",
    ),
    Recipe(
        name="Chocolate Curl",
        description=(
            "Elegant curled shavings of chocolate used to garnish cakes, "
            "mousses, and plated desserts."
        ),
        ingredients=[
            Ingredient("dark or milk chocolate block", "100 g", "room temperature"),
        ],
        steps=[
            "Bring the chocolate to room temperature (18–20 °C); it must be "
            "pliable but not melted.",
            "Hold the chocolate block firmly and draw a vegetable peeler along "
            "the flat edge in long, confident strokes.",
            "Collect the curls on a cold parchment-lined tray.",
            "Refrigerate immediately and handle with a toothpick or skewer to "
            "avoid melting from hand heat.",
        ],
        difficulty=DifficultyLevel.EASY,
        prep_time_minutes=10,
        tags=["chocolate", "dessert", "no-cook"],
        yield_description="approximately 20 curls",
    ),
    Recipe(
        name="Strawberry Fan",
        description=(
            "A sliced strawberry fanned open to create a decorative flower "
            "shape for dessert plates and fruit platters."
        ),
        ingredients=[
            Ingredient("fresh strawberries", "1 per serving", "hull on, firm"),
        ],
        steps=[
            "Place the strawberry hull-side down on a cutting board.",
            "Starting just below the hull, make parallel cuts down to the tip, "
            "spacing cuts about 3 mm apart. Do not cut through the hull.",
            "Gently press the strawberry from the sides so the slices fan out.",
            "Place flat-side down on the plate and arrange the fan open.",
        ],
        difficulty=DifficultyLevel.EASY,
        prep_time_minutes=2,
        tags=["fruit", "strawberry", "dessert", "no-cook"],
        yield_description="1 fan per strawberry",
    ),
    Recipe(
        name="Cucumber Ribbon",
        description=(
            "Long translucent ribbons of cucumber that add freshness and "
            "elegance to salads, seafood dishes, and canapés."
        ),
        ingredients=[
            Ingredient("English cucumber", "1 whole", "ends trimmed"),
        ],
        steps=[
            "Run a vegetable peeler along the length of the cucumber to create "
            "wide, thin ribbons.",
            "Discard the first ribbon if it includes too much skin.",
            "Lay the ribbons flat or fold them into loose rosettes.",
            "Submerge in ice water for 5 minutes to firm the ribbons before plating.",
        ],
        difficulty=DifficultyLevel.EASY,
        prep_time_minutes=8,
        tags=["vegetable", "cucumber", "savoury", "no-cook"],
        yield_description="12–16 ribbons per cucumber",
    ),
    Recipe(
        name="Tuile Biscuit",
        description=(
            "A thin, crisp baked wafer that can be shaped while warm to create "
            "dramatic sculptural garnishes for desserts and savoury dishes."
        ),
        ingredients=[
            Ingredient("unsalted butter", "60 g", "melted and cooled"),
            Ingredient("icing sugar", "60 g", "sifted"),
            Ingredient("plain flour", "60 g", "sifted"),
            Ingredient("egg whites", "2 large", "lightly beaten"),
            Ingredient("vanilla extract", "½ tsp", "optional"),
        ],
        steps=[
            "Preheat the oven to 180 °C (fan 160 °C). Line a baking sheet with "
            "a silicone mat or greased parchment.",
            "Mix butter, icing sugar, and flour together until smooth. "
            "Fold in egg whites and vanilla until a thin batter forms.",
            "Spread tablespoon-sized rounds onto the prepared sheet, leaving "
            "5 cm between each.",
            "Bake for 6–8 minutes until golden at the edges.",
            "Working quickly while hot, drape each tuile over a rolling pin or "
            "small bowl to curve it; cool completely before storing.",
        ],
        difficulty=DifficultyLevel.INTERMEDIATE,
        prep_time_minutes=25,
        tags=["baked", "sweet", "dessert", "sculptural"],
        yield_description="12–14 tuiles",
    ),
    Recipe(
        name="Micro Herb Bouquet",
        description=(
            "A tiny cluster of mixed micro herbs and edible flowers arranged "
            "as a delicate, flavour-packed centrepiece garnish."
        ),
        ingredients=[
            Ingredient("micro basil", "small pinch"),
            Ingredient("micro shiso", "small pinch"),
            Ingredient("micro cress", "small pinch"),
            Ingredient("edible flowers (pansies or violas)", "2–3 flowers"),
        ],
        steps=[
            "Keep all herbs refrigerated until the last moment to maintain "
            "freshness and colour.",
            "Select 3–5 stems of each herb variety.",
            "Group them together by height, tallest stems in the centre.",
            "Bind very loosely at the base with a strip of blanched chive or "
            "a tiny piece of food-safe string.",
            "Place upright on the dish just before serving.",
        ],
        difficulty=DifficultyLevel.INTERMEDIATE,
        prep_time_minutes=10,
        tags=["herb", "flowers", "edible flowers", "savoury", "no-cook"],
        yield_description="1 bouquet per serving",
    ),
    Recipe(
        name="Dehydrated Citrus Wheel",
        description=(
            "Thin slices of citrus dried in a low oven to produce translucent, "
            "jewel-like decorations for cocktails and desserts."
        ),
        ingredients=[
            Ingredient("lemons, limes, or blood oranges", "2 whole", "thinly sliced"),
        ],
        steps=[
            "Preheat oven to 80 °C. Line a baking sheet with a wire rack.",
            "Slice citrus into 3 mm rounds and pat dry with kitchen paper.",
            "Arrange in a single layer on the rack.",
            "Dry in the oven for 3–4 hours, turning once, until completely "
            "dehydrated and slightly translucent.",
            "Cool completely and store in an airtight container at room "
            "temperature for up to 2 weeks.",
        ],
        difficulty=DifficultyLevel.EASY,
        prep_time_minutes=240,
        tags=["citrus", "dehydrated", "cocktail", "dessert"],
        yield_description="20–30 wheels",
    ),
    Recipe(
        name="Radish Rose",
        description=(
            "A whole radish carved into a rose shape that blooms when soaked "
            "in ice water, adding colour to cheese boards and salad platters."
        ),
        ingredients=[
            Ingredient("firm radishes", "1 per rose", "tops trimmed, root left on"),
        ],
        steps=[
            "Using a small paring knife, make 4 shallow curved cuts around the "
            "equator of the radish, cutting from the outside towards the centre "
            "without going all the way through.",
            "Make a second row of cuts just above the first, offsetting by 45°.",
            "Add a third row near the top if the radish is large enough.",
            "Submerge in ice water and refrigerate for at least 1 hour; the "
            'petals will open like a rose as the cuts "bloom".',
        ],
        difficulty=DifficultyLevel.INTERMEDIATE,
        prep_time_minutes=70,
        tags=["vegetable", "radish", "carving", "savoury"],
        yield_description="1 rose per radish",
    ),
    Recipe(
        name="Spun Sugar Nest",
        description=(
            "Delicate golden threads of caramelised sugar spun into an airy "
            "nest or halo — a showstopping garnish for plated desserts."
        ),
        ingredients=[
            Ingredient("caster sugar", "200 g"),
            Ingredient("liquid glucose", "50 g"),
            Ingredient("water", "60 ml"),
        ],
        steps=[
            "Combine sugar, glucose, and water in a heavy-based saucepan over "
            "medium heat. Stir until the sugar dissolves, then stop stirring.",
            "Boil to 155 °C (hard-crack stage) using a sugar thermometer.",
            "Remove from heat and let bubbles subside for 1 minute.",
            "Lightly oil two wooden spoon handles and rest them over a work "
            "surface, handles extending over the edge.",
            "Dip a fork into the syrup and quickly wave it back and forth over "
            "the handles to form fine golden threads.",
            "Gather threads gently and shape into nests. Use immediately — "
            "spun sugar dissolves in humidity.",
        ],
        difficulty=DifficultyLevel.ADVANCED,
        prep_time_minutes=30,
        tags=["sugar", "dessert", "showstopper", "advanced"],
        yield_description="6–8 nests",
    ),
]

# Build an index by name for fast lookup
_RECIPE_INDEX: Dict[str, Recipe] = {r.name.lower(): r for r in _RECIPES}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def all_recipes() -> List[Recipe]:
    """Return all available garnish recipes."""
    return list(_RECIPES)


def get_recipe(name: str) -> Optional[Recipe]:
    """Return the recipe with the given name (case-insensitive), or None."""
    return _RECIPE_INDEX.get(name.lower())


def recipes_by_difficulty(difficulty: DifficultyLevel) -> List[Recipe]:
    """Return all recipes matching the given difficulty level."""
    return [r for r in _RECIPES if r.difficulty == difficulty]


def recipes_by_tag(tag: str) -> List[Recipe]:
    """Return all recipes that include the given tag (case-insensitive)."""
    tag_lower = tag.lower()
    return [r for r in _RECIPES if tag_lower in [t.lower() for t in r.tags]]


def recipes_by_max_time(minutes: int) -> List[Recipe]:
    """Return all recipes whose prep time is at most *minutes*."""
    return [r for r in _RECIPES if r.prep_time_minutes <= minutes]
