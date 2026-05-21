"""Preparation techniques for culinary garnishes."""

from __future__ import annotations

from typing import Dict, List, Optional

from .models import DifficultyLevel, Technique

# ---------------------------------------------------------------------------
# Technique catalogue
# ---------------------------------------------------------------------------

_TECHNIQUES: List[Technique] = [
    Technique(
        name="Chiffonade",
        description=(
            "A knife technique that produces fine, ribbon-like strips from "
            "leafy herbs or vegetables by stacking, rolling, and slicing."
        ),
        steps=[
            "Select large, flat leaves (basil, mint, sage, or sorrel). "
            "Remove any thick stems.",
            "Stack the leaves in a neat pile with the largest leaf on the bottom.",
            "Roll the stack into a tight cylinder, working from the stem end.",
            "Hold the cylinder firmly and slice across it with a sharp chef's "
            "knife in cuts 1–2 mm wide.",
            "Gently fluff the ribbons apart with your fingertips.",
        ],
        difficulty=DifficultyLevel.EASY,
        tools_required=["chef's knife", "cutting board"],
        applicable_to=["basil", "mint", "sage", "sorrel", "spinach", "kaffir lime leaves"],
        tips=[
            "Use immediately after cutting to prevent oxidation and browning.",
            "A very sharp knife prevents bruising, which darkens the leaves.",
            "For maximum length, align the roll perpendicular to the direction of cut.",
        ],
    ),
    Technique(
        name="Julienne",
        description=(
            "A cutting technique that reduces vegetables or citrus peel into "
            "thin matchstick strips for delicate, uniform garnishes."
        ),
        steps=[
            "Peel the vegetable or fruit (e.g., carrot, cucumber, or citrus rind) "
            "and trim into a rectangular block.",
            "Slice the block into planks 2–3 mm thick.",
            "Stack the planks and cut lengthwise into sticks 2–3 mm wide.",
            "All strips should be uniform in width, length, and thickness.",
        ],
        difficulty=DifficultyLevel.INTERMEDIATE,
        tools_required=["chef's knife or mandoline", "cutting board", "ruler (optional)"],
        applicable_to=["carrot", "cucumber", "zucchini", "leek", "citrus peel", "ginger"],
        tips=[
            "A mandoline slicer produces the most uniform planks.",
            "Blanch vegetable julienne in salted boiling water for 30 seconds "
            "and shock in ice water to soften and set the colour.",
            "Keep julienne in cold water to prevent drying out before serving.",
        ],
    ),
    Technique(
        name="Brunoise",
        description=(
            "An ultra-fine dice (1–2 mm cubes) used to create neat, jewel-like "
            "garnishes from vegetables, fruits, or herbs."
        ),
        steps=[
            "Julienne the ingredient to 1–2 mm strips as per the julienne technique.",
            "Gather the strips into a tight bundle and rotate 90°.",
            "Slice across the bundle in 1–2 mm intervals to produce tiny cubes.",
            "Rinse under cold water to remove any starch or residue.",
        ],
        difficulty=DifficultyLevel.ADVANCED,
        tools_required=["chef's knife", "cutting board"],
        applicable_to=["carrot", "celery", "red pepper", "cucumber", "mango", "apple"],
        tips=[
            "Consistent julienne is the key to uniform brunoise — do not rush the first step.",
            "Chill the ingredient before cutting to make it firmer and easier to dice.",
        ],
    ),
    Technique(
        name="Blanching and Shocking",
        description=(
            "A two-stage technique that briefly cooks garnish ingredients in "
            "boiling water then immediately halts cooking in ice water, "
            "locking in vibrant colour and a tender-crisp texture."
        ),
        steps=[
            "Bring a large pot of well-salted water to a rolling boil.",
            "Prepare an ice bath: a bowl of cold water with plenty of ice.",
            "Add the prepared garnish ingredient (herbs, vegetables) to the "
            "boiling water and cook for 30–90 seconds depending on thickness.",
            "Using a spider or slotted spoon, transfer immediately to the ice bath.",
            "Leave in the ice bath for the same duration as the blanching time.",
            "Drain and pat dry on kitchen paper before use.",
        ],
        difficulty=DifficultyLevel.EASY,
        tools_required=["large saucepan", "spider or slotted spoon", "large bowl", "ice"],
        applicable_to=["herbs", "green beans", "asparagus", "peas", "leafy greens"],
        tips=[
            "Salt the blanching water generously — it seasons the ingredient and "
            "raises the boiling point for a better colour result.",
            "Work in small batches so the water returns to the boil quickly.",
            "Dry the ingredient thoroughly before using as a garnish so excess "
            "water does not dilute sauces.",
        ],
    ),
    Technique(
        name="Dehydration",
        description=(
            "Low-temperature oven or dehydrator drying that removes moisture "
            "from fruits, vegetables, and herbs to create lightweight, "
            "shelf-stable, intensely flavoured garnishes."
        ),
        steps=[
            "Slice the ingredient uniformly (2–4 mm) for even drying.",
            "Pat each slice dry with kitchen paper to remove surface moisture.",
            "Arrange in a single layer on a wire rack set inside a baking tray, "
            "or in a food dehydrator.",
            "Dry at 70–90 °C (oven) or the dehydrator's recommended setting "
            "until completely dry and brittle (2–8 hours depending on ingredient).",
            "Cool completely before storing in an airtight container.",
        ],
        difficulty=DifficultyLevel.EASY,
        tools_required=["oven or food dehydrator", "wire rack", "baking tray", "mandoline (optional)"],
        applicable_to=["citrus slices", "strawberries", "mushrooms", "tomatoes", "herbs"],
        tips=[
            "A mandoline ensures uniform thickness for even drying.",
            "Store dehydrated garnishes with a silica gel packet to absorb moisture.",
            "Low and slow is key — too high a temperature causes browning rather than drying.",
        ],
    ),
    Technique(
        name="Piping",
        description=(
            "Using a piping bag fitted with a decorative nozzle to apply "
            "creams, mousses, purées, and sauces in precise, elegant shapes."
        ),
        steps=[
            "Fit the piping bag with the desired nozzle (star, round, petal, etc.).",
            "Fill the bag no more than two-thirds full to maintain control.",
            "Twist the open end to seal and push the mixture towards the tip.",
            "Hold the bag with your dominant hand at the twist, guide with the other.",
            "Apply steady, even pressure to pipe the desired shape.",
            "Stop pressure before lifting the nozzle to avoid a tail.",
        ],
        difficulty=DifficultyLevel.INTERMEDIATE,
        tools_required=["piping bag", "piping nozzles", "palette knife"],
        applicable_to=["whipped cream", "crème chantilly", "ganache", "purées", "soft cheese"],
        tips=[
            "Chill the filled piping bag for 10 minutes before use if the "
            "mixture is very soft.",
            "Practice consistent pressure on a plate or parchment before piping "
            "directly onto the dish.",
            "Warm hands can melt cream-based mixtures — swap bags or chill "
            "hands frequently.",
        ],
    ),
    Technique(
        name="Sugar Work — Pulling and Blowing",
        description=(
            "An advanced confectionery technique where cooked sugar is "
            "repeatedly pulled or blown to produce shiny, translucent petals, "
            "ribbons, and sculptural decorations."
        ),
        steps=[
            "Cook sugar syrup (sugar, glucose, water) to 155–160 °C.",
            "Pour onto a silicone mat and fold the edges inward as it cools.",
            "Under a heat lamp, pull and fold the sugar mass repeatedly until "
            "it becomes satin-smooth and glossy.",
            "For pulling: stretch the mass into ribbons or petals using both "
            "hands, working quickly.",
            "For blowing: attach a small ball of pulled sugar to a sugar-blowing "
            "pump and inflate gently to form a hollow sphere or petal.",
            "Allow shapes to cool and harden completely before assembling.",
        ],
        difficulty=DifficultyLevel.ADVANCED,
        tools_required=["sugar thermometer", "silicone mat", "heat lamp", "sugar-blowing pump (for blowing)", "gloves"],
        applicable_to=["sugar showpieces", "dessert centrepieces", "celebration cakes"],
        tips=[
            "Wear food-safe silicone gloves — pulled sugar is extremely hot.",
            "Humidity is the enemy of sugar work; work in a dry environment.",
            "Colour the sugar with gel food colouring added during cooking for "
            "vibrant, even hues.",
        ],
    ),
    Technique(
        name="Quenelle",
        description=(
            "A three-sided oval shape formed by repeatedly passing a mixture "
            "between two warm spoons, used for creams, ice creams, and mousses."
        ),
        steps=[
            "Use two oval tablespoons dipped in warm water.",
            "Scoop a generous spoonful of the chilled mixture with the first spoon.",
            "Pass the mixture from the first spoon to the second in a smooth "
            "scooping motion, rotating to create the first smooth face.",
            "Pass back to the first spoon, rotating again to form the second face.",
            "Repeat until the quenelle has three smooth, even sides and pointed ends.",
            "Place on the dish using the last spoon used, pointed ends at the sides.",
        ],
        difficulty=DifficultyLevel.INTERMEDIATE,
        tools_required=["two oval tablespoons", "warm water"],
        applicable_to=["ice cream", "sorbet", "whipped cream", "mousse", "crème fraîche"],
        tips=[
            "Cold mixture is essential — work quickly before heat from your hands "
            "melts the quenelle.",
            "Dip spoons in warm (not hot) water between passes to prevent sticking.",
            "Practice with mashed potato before moving to delicate creams.",
        ],
    ),
]

# Build an index by name for fast lookup
_TECHNIQUE_INDEX: Dict[str, Technique] = {t.name.lower(): t for t in _TECHNIQUES}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def all_techniques() -> List[Technique]:
    """Return all available preparation techniques."""
    return list(_TECHNIQUES)


def get_technique(name: str) -> Optional[Technique]:
    """Return the technique with the given name (case-insensitive), or None."""
    return _TECHNIQUE_INDEX.get(name.lower())


def techniques_by_difficulty(difficulty: DifficultyLevel) -> List[Technique]:
    """Return all techniques matching the given difficulty level."""
    return [t for t in _TECHNIQUES if t.difficulty == difficulty]


def techniques_for_ingredient(ingredient: str) -> List[Technique]:
    """Return techniques that list the given ingredient as applicable (case-insensitive)."""
    ingredient_lower = ingredient.lower()
    return [
        t for t in _TECHNIQUES
        if any(ingredient_lower in item.lower() for item in t.applicable_to)
    ]
