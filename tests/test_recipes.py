"""Tests for the recipes module."""

import pytest

from garnish import (
    DifficultyLevel,
    Recipe,
    all_recipes,
    get_recipe,
    recipes_by_difficulty,
    recipes_by_max_time,
    recipes_by_tag,
)


class TestAllRecipes:
    def test_returns_list(self):
        result = all_recipes()
        assert isinstance(result, list)

    def test_non_empty(self):
        assert len(all_recipes()) > 0

    def test_all_items_are_recipes(self):
        for recipe in all_recipes():
            assert isinstance(recipe, Recipe)

    def test_each_recipe_has_required_fields(self):
        for recipe in all_recipes():
            assert recipe.name
            assert recipe.description
            assert len(recipe.ingredients) > 0
            assert len(recipe.steps) > 0
            assert isinstance(recipe.difficulty, DifficultyLevel)
            assert recipe.prep_time_minutes > 0

    def test_returns_independent_copy(self):
        """Mutating the returned list must not affect the catalogue."""
        first = all_recipes()
        first.clear()
        second = all_recipes()
        assert len(second) > 0


class TestGetRecipe:
    def test_returns_recipe_by_exact_name(self):
        recipe = get_recipe("Citrus Twist")
        assert recipe is not None
        assert recipe.name == "Citrus Twist"

    def test_case_insensitive(self):
        assert get_recipe("citrus twist") is not None
        assert get_recipe("CITRUS TWIST") is not None
        assert get_recipe("Citrus Twist") is not None

    def test_returns_none_for_unknown(self):
        assert get_recipe("Nonexistent Garnish XYZ") is None

    def test_known_recipes_are_retrievable(self):
        for recipe in all_recipes():
            found = get_recipe(recipe.name)
            assert found is not None
            assert found.name == recipe.name


class TestRecipesByDifficulty:
    def test_easy_recipes_exist(self):
        easy = recipes_by_difficulty(DifficultyLevel.EASY)
        assert len(easy) > 0
        for r in easy:
            assert r.difficulty == DifficultyLevel.EASY

    def test_intermediate_recipes_exist(self):
        intermediate = recipes_by_difficulty(DifficultyLevel.INTERMEDIATE)
        assert len(intermediate) > 0
        for r in intermediate:
            assert r.difficulty == DifficultyLevel.INTERMEDIATE

    def test_advanced_recipes_exist(self):
        advanced = recipes_by_difficulty(DifficultyLevel.ADVANCED)
        assert len(advanced) > 0
        for r in advanced:
            assert r.difficulty == DifficultyLevel.ADVANCED

    def test_all_difficulties_partition_catalogue(self):
        easy = recipes_by_difficulty(DifficultyLevel.EASY)
        intermediate = recipes_by_difficulty(DifficultyLevel.INTERMEDIATE)
        advanced = recipes_by_difficulty(DifficultyLevel.ADVANCED)
        assert len(easy) + len(intermediate) + len(advanced) == len(all_recipes())


class TestRecipesByTag:
    def test_citrus_tag_returns_results(self):
        results = recipes_by_tag("citrus")
        assert len(results) > 0
        for r in results:
            assert "citrus" in [t.lower() for t in r.tags]

    def test_tag_is_case_insensitive(self):
        lower = recipes_by_tag("dessert")
        upper = recipes_by_tag("DESSERT")
        assert lower == upper

    def test_unknown_tag_returns_empty(self):
        assert recipes_by_tag("not_a_real_tag_xyz") == []

    def test_no_cook_tag(self):
        results = recipes_by_tag("no-cook")
        assert len(results) > 0


class TestRecipesByMaxTime:
    def test_returns_only_recipes_within_time(self):
        results = recipes_by_max_time(10)
        for r in results:
            assert r.prep_time_minutes <= 10

    def test_very_long_time_returns_all(self):
        assert len(recipes_by_max_time(10_000)) == len(all_recipes())

    def test_zero_minutes_returns_empty(self):
        # No recipe should have 0 prep time
        assert recipes_by_max_time(0) == []


class TestRecipeSummary:
    def test_summary_contains_name(self):
        recipe = get_recipe("Citrus Twist")
        summary = recipe.summary()
        assert "Citrus Twist" in summary

    def test_summary_contains_ingredients(self):
        recipe = get_recipe("Tuile Biscuit")
        summary = recipe.summary()
        for ingredient in recipe.ingredients:
            assert ingredient.name in summary

    def test_summary_contains_steps(self):
        recipe = get_recipe("Citrus Twist")
        summary = recipe.summary()
        for step in recipe.steps:
            assert step in summary

    def test_str_representation(self):
        recipe = get_recipe("Citrus Twist")
        text = str(recipe)
        assert "Citrus Twist" in text
        assert "easy" in text
