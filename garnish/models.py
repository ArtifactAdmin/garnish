"""Data models for culinary garnishes."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class DifficultyLevel(str, Enum):
    """Skill level required to execute a garnish or technique."""

    EASY = "easy"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class PlatingZone(str, Enum):
    """Region of the plate where a garnish element is placed."""

    CENTER = "center"
    RIM = "rim"
    SIDE = "side"
    TOP = "top"
    SAUCE = "sauce"


@dataclass
class Ingredient:
    """A single ingredient used in a garnish recipe."""

    name: str
    quantity: str
    notes: Optional[str] = None

    def __str__(self) -> str:
        if self.notes:
            return f"{self.quantity} {self.name} ({self.notes})"
        return f"{self.quantity} {self.name}"


@dataclass
class Recipe:
    """A recipe for preparing a culinary garnish."""

    name: str
    description: str
    ingredients: List[Ingredient]
    steps: List[str]
    difficulty: DifficultyLevel
    prep_time_minutes: int
    tags: List[str] = field(default_factory=list)
    yield_description: str = "1 garnish"

    def __str__(self) -> str:
        return f"Recipe: {self.name} ({self.difficulty.value}, {self.prep_time_minutes} min)"

    def summary(self) -> str:
        """Return a short human-readable summary of the recipe."""
        lines = [
            f"=== {self.name} ===",
            self.description,
            f"Difficulty: {self.difficulty.value.capitalize()}",
            f"Prep time: {self.prep_time_minutes} minutes",
            f"Yield: {self.yield_description}",
            "",
            "Ingredients:",
        ]
        for ingredient in self.ingredients:
            lines.append(f"  - {ingredient}")
        lines.append("")
        lines.append("Steps:")
        for i, step in enumerate(self.steps, start=1):
            lines.append(f"  {i}. {step}")
        if self.tags:
            lines.append("")
            lines.append(f"Tags: {', '.join(self.tags)}")
        return "\n".join(lines)


@dataclass
class Technique:
    """A preparation technique used to create culinary garnishes."""

    name: str
    description: str
    steps: List[str]
    difficulty: DifficultyLevel
    tools_required: List[str] = field(default_factory=list)
    applicable_to: List[str] = field(default_factory=list)
    tips: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        return f"Technique: {self.name} ({self.difficulty.value})"

    def summary(self) -> str:
        """Return a short human-readable summary of the technique."""
        lines = [
            f"=== {self.name} ===",
            self.description,
            f"Difficulty: {self.difficulty.value.capitalize()}",
        ]
        if self.tools_required:
            lines.append(f"Tools: {', '.join(self.tools_required)}")
        if self.applicable_to:
            lines.append(f"Applicable to: {', '.join(self.applicable_to)}")
        lines.append("")
        lines.append("Steps:")
        for i, step in enumerate(self.steps, start=1):
            lines.append(f"  {i}. {step}")
        if self.tips:
            lines.append("")
            lines.append("Tips:")
            for tip in self.tips:
                lines.append(f"  * {tip}")
        return "\n".join(lines)


@dataclass
class PlatingElement:
    """A single element placed on the plate as part of a plating guide."""

    garnish_name: str
    zone: PlatingZone
    quantity: str
    placement_notes: str


@dataclass
class PlatingGuide:
    """Guidelines for plating a dish with culinary garnishes."""

    dish_name: str
    description: str
    elements: List[PlatingElement]
    color_notes: str = ""
    texture_notes: str = ""
    height_notes: str = ""
    general_tips: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        return f"PlatingGuide: {self.dish_name}"

    def summary(self) -> str:
        """Return a short human-readable summary of the plating guide."""
        lines = [
            f"=== Plating Guide: {self.dish_name} ===",
            self.description,
            "",
            "Elements:",
        ]
        for el in self.elements:
            lines.append(
                f"  - {el.garnish_name} ({el.zone.value}): "
                f"{el.quantity} — {el.placement_notes}"
            )
        if self.color_notes:
            lines.append(f"\nColor: {self.color_notes}")
        if self.texture_notes:
            lines.append(f"Texture: {self.texture_notes}")
        if self.height_notes:
            lines.append(f"Height: {self.height_notes}")
        if self.general_tips:
            lines.append("\nGeneral Tips:")
            for tip in self.general_tips:
                lines.append(f"  * {tip}")
        return "\n".join(lines)
