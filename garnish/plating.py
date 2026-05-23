"""Plating guidelines for culinary garnishes."""

from __future__ import annotations

from typing import Dict, List, Optional

from .models import PlatingElement, PlatingGuide, PlatingZone

# ---------------------------------------------------------------------------
# Plating guide catalogue
# ---------------------------------------------------------------------------

_GUIDES: List[PlatingGuide] = [
    PlatingGuide(
        dish_name="Pan-Seared Salmon Fillet",
        description=(
            "A restaurant-style presentation for a golden-crusted salmon fillet "
            "on a bed of purée, finished with crisp vegetable garnishes."
        ),
        elements=[
            PlatingElement(
                garnish_name="Cucumber Ribbon",
                zone=PlatingZone.SIDE,
                quantity="2–3 ribbons",
                placement_notes=(
                    "Fold each ribbon into a loose rosette and place to the left "
                    "of the fillet to add freshness and height contrast."
                ),
            ),
            PlatingElement(
                garnish_name="Herb Chiffonade",
                zone=PlatingZone.TOP,
                quantity="small pinch",
                placement_notes=(
                    "Scatter lightly over the top of the fillet just before serving "
                    "for colour and aroma."
                ),
            ),
            PlatingElement(
                garnish_name="Citrus Twist",
                zone=PlatingZone.RIM,
                quantity="1 twist",
                placement_notes=(
                    "Rest a lemon twist against the fillet on the right side; "
                    "it acts as a flavour signal and a pop of yellow."
                ),
            ),
        ],
        color_notes=(
            "The golden-brown crust of the salmon contrasts with the green cucumber "
            "and herb chiffonade. The lemon twist introduces a bright yellow accent."
        ),
        texture_notes=(
            "Crisp cucumber ribbons counterbalance the soft, flaky texture of the salmon. "
            "The delicate herb strips add a fine, feathery element."
        ),
        height_notes=(
            "Keep the ribbon rosettes at medium height (3–4 cm). "
            "The fillet itself provides the dominant height on the plate."
        ),
        general_tips=[
            "Place the salmon slightly off-centre to leave negative space for garnishes.",
            "Use a squeeze bottle to add dots of lemon beurre blanc on the rim for extra elegance.",
            "Always add heat-sensitive herbs last, after all hot components are plated.",
        ],
    ),
    PlatingGuide(
        dish_name="Chocolate Fondant with Vanilla Ice Cream",
        description=(
            "A classic patisserie plating combining a warm, molten chocolate "
            "fondant with cold vanilla ice cream and decorative confectionery garnishes."
        ),
        elements=[
            PlatingElement(
                garnish_name="Vanilla Ice Cream Quenelle",
                zone=PlatingZone.SIDE,
                quantity="1 quenelle",
                placement_notes=(
                    "Form a quenelle and place it to the right of the fondant, "
                    "resting on the sauce. Serve immediately to prevent melting."
                ),
            ),
            PlatingElement(
                garnish_name="Chocolate Curl",
                zone=PlatingZone.TOP,
                quantity="3–4 curls",
                placement_notes=(
                    "Stack curls loosely on top of the fondant at varying angles "
                    "to create height and a sense of movement."
                ),
            ),
            PlatingElement(
                garnish_name="Spun Sugar Nest",
                zone=PlatingZone.TOP,
                quantity="1 small nest",
                placement_notes=(
                    "Perch the nest on top of the chocolate curls. "
                    "Add last — spun sugar dissolves with moisture and heat."
                ),
            ),
            PlatingElement(
                garnish_name="Dehydrated Citrus Wheel",
                zone=PlatingZone.SAUCE,
                quantity="1 wheel",
                placement_notes=(
                    "Lay a blood orange wheel flat in the chocolate sauce to "
                    "add a jewel-like colour contrast."
                ),
            ),
        ],
        color_notes=(
            "Deep brown fondant and sauce pair with ivory ice cream. "
            "The golden spun sugar and ruby-red citrus wheel provide vivid contrast."
        ),
        texture_notes=(
            "Contrasting temperatures and textures are key: molten hot fondant, "
            "cold creamy ice cream, airy spun sugar, and crunchy chocolate curls."
        ),
        height_notes=(
            "Build height vertically on the fondant: curls first, then the spun "
            "sugar nest. Keep the ice cream quenelle lower to emphasise contrast."
        ),
        general_tips=[
            "Pre-prepare all garnishes; assembly should take under 60 seconds "
            "so the fondant does not overcook while resting.",
            "Warm the plate briefly so the sauce spreads naturally when the "
            "fondant is unmoulded onto it.",
            "Use a squeeze bottle to create an arc of raspberry coulis on the "
            "rim for an additional colour and flavour element.",
        ],
    ),
    PlatingGuide(
        dish_name="Mezze Platter",
        description=(
            "A vibrant sharing platter of Middle Eastern dips and vegetables, "
            "elevated with colourful vegetable garnishes and herb decorations."
        ),
        elements=[
            PlatingElement(
                garnish_name="Radish Rose",
                zone=PlatingZone.CENTER,
                quantity="2–3 roses",
                placement_notes=(
                    "Cluster the radish roses in the centre of the platter as a "
                    "focal point, varying heights if possible."
                ),
            ),
            PlatingElement(
                garnish_name="Cucumber Ribbon",
                zone=PlatingZone.RIM,
                quantity="6–8 ribbons",
                placement_notes=(
                    "Roll ribbons into cylinders and stand them upright around "
                    "the perimeter of the platter for a border effect."
                ),
            ),
            PlatingElement(
                garnish_name="Herb Chiffonade",
                zone=PlatingZone.TOP,
                quantity="2 tbsp",
                placement_notes=(
                    "Scatter over the hummus and baba ganoush for colour and aroma. "
                    "Use mint over tabbouleh and parsley over hummus."
                ),
            ),
            PlatingElement(
                garnish_name="Micro Herb Bouquet",
                zone=PlatingZone.SIDE,
                quantity="1–2 bouquets",
                placement_notes=(
                    "Tuck micro herb bouquets beside the dips for a fine-dining "
                    "touch, ensuring they stand upright."
                ),
            ),
        ],
        color_notes=(
            "The platter relies on the contrast between the ivory and beige dips, "
            "the deep-pink radish roses, vibrant green cucumber and herbs, and the "
            "jewel tones of any edible flowers in the bouquet."
        ),
        texture_notes=(
            "Smooth dips are contrasted with the crisp cucumber rolls and the "
            "delicate, feathery micro herbs."
        ),
        height_notes=(
            "Stand cucumber rolls upright for vertical interest. Keep the radish "
            "roses at the natural height of the vegetable (4–5 cm)."
        ),
        general_tips=[
            "Chill the platter in the refrigerator for 15 minutes before assembly "
            "to keep garnishes fresh longer.",
            "Use odd numbers of garnish elements for a more natural, artistic look.",
            "Add a drizzle of extra virgin olive oil over the dips just before "
            "serving to create sheen and depth.",
        ],
    ),
    PlatingGuide(
        dish_name="Classic Gin and Tonic",
        description=(
            "An elegant garnished serve of gin and tonic in a balloon glass, "
            "with aromatic and visual garnishes chosen to complement the botanicals."
        ),
        elements=[
            PlatingElement(
                garnish_name="Citrus Twist",
                zone=PlatingZone.RIM,
                quantity="1 twist",
                placement_notes=(
                    "Gently express the lemon or lime twist over the glass to "
                    "release the oils, then hook it over the rim or drop it in."
                ),
            ),
            PlatingElement(
                garnish_name="Dehydrated Citrus Wheel",
                zone=PlatingZone.SAUCE,
                quantity="1 wheel",
                placement_notes=(
                    "Float a dehydrated lime wheel on the surface of the drink "
                    "as a decorative, aromatic element."
                ),
            ),
            PlatingElement(
                garnish_name="Herb Sprig",
                zone=PlatingZone.RIM,
                quantity="1 sprig",
                placement_notes=(
                    "Rest a sprig of fresh rosemary or thyme across the rim or "
                    "inside the glass so it infuses subtly into the drink."
                ),
            ),
        ],
        color_notes=(
            "Clear tonic and ice provide a neutral canvas. The green citrus twist "
            "and herb sprig, and the yellow-green dehydrated wheel, bring life and "
            "brightness to the glass."
        ),
        texture_notes=(
            "Garnishes are visual and aromatic here; texture is less critical. "
            "Focus on freshness and fragrance."
        ),
        height_notes=(
            "Keep garnishes at or just above the rim of the glass. "
            "Do not crowd the opening — leave room for the nose of the drinker "
            "to engage with the aromas."
        ),
        general_tips=[
            "Match citrus garnish to the dominant botanical of the gin: "
            "lemon for floral gins, lime for citrus-forward gins.",
            "Lightly bruise the herb sprig between your fingers before placing "
            "to release its aromatic oils.",
            "Chill the garnishes in the refrigerator before use — cold garnishes "
            "help maintain the temperature of the drink.",
        ],
    ),
    PlatingGuide(
        dish_name="Strawberry Panna Cotta",
        description=(
            "A silky panna cotta served with fresh strawberry garnishes and "
            "delicate tuile biscuits for textural contrast."
        ),
        elements=[
            PlatingElement(
                garnish_name="Strawberry Fan",
                zone=PlatingZone.TOP,
                quantity="1 fan",
                placement_notes=(
                    "Place a single strawberry fan on top of the unmoulded panna "
                    "cotta at a slight angle as the primary garnish."
                ),
            ),
            PlatingElement(
                garnish_name="Tuile Biscuit",
                zone=PlatingZone.SIDE,
                quantity="1 tuile",
                placement_notes=(
                    "Lean a curved tuile against the side of the panna cotta "
                    "to create height and a crisp element."
                ),
            ),
            PlatingElement(
                garnish_name="Micro Herb Bouquet",
                zone=PlatingZone.SIDE,
                quantity="1 small bouquet",
                placement_notes=(
                    "Tuck a tiny bouquet of micro mint beside the panna cotta "
                    "for colour and aroma."
                ),
            ),
        ],
        color_notes=(
            "Ivory panna cotta is the backdrop for the vivid red strawberry fan. "
            "The golden tuile and green micro mint add complementary accent colours."
        ),
        texture_notes=(
            "The wobbling, silky panna cotta contrasts with the crisp tuile and "
            "the juicy strawberry. Micro herbs add a feathery delicacy."
        ),
        height_notes=(
            "The tuile provides the tallest element. Keep the strawberry fan and "
            "herb bouquet at plate level to guide the eye upward to the tuile."
        ),
        general_tips=[
            "Unmould the panna cotta directly onto the plate and garnish within "
            "30 seconds to prevent condensation pooling.",
            "A mirror of strawberry coulis on the base before unmoulding adds "
            "colour depth and a flavour boost.",
            "Dust the tuile lightly with icing sugar just before serving for a "
            "professional finish.",
        ],
    ),
]

# Build an index by dish name for fast lookup
_GUIDE_INDEX: Dict[str, PlatingGuide] = {g.dish_name.lower(): g for g in _GUIDES}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def all_guides() -> List[PlatingGuide]:
    """Return all available plating guides."""
    return list(_GUIDES)


def get_guide(dish_name: str) -> Optional[PlatingGuide]:
    """Return the plating guide for the given dish name (case-insensitive), or None."""
    return _GUIDE_INDEX.get(dish_name.lower())


def guides_by_garnish(garnish_name: str) -> List[PlatingGuide]:
    """Return plating guides that feature the given garnish (case-insensitive)."""
    garnish_lower = garnish_name.lower()
    return [
        g for g in _GUIDES
        if any(garnish_lower in el.garnish_name.lower() for el in g.elements)
    ]


def guides_by_zone(zone: PlatingZone) -> List[PlatingGuide]:
    """Return plating guides that include at least one element in the given zone."""
    return [g for g in _GUIDES if any(el.zone == zone for el in g.elements)]
