"""Tests for the techniques module."""

import pytest

from garnish import (
    DifficultyLevel,
    Technique,
    all_techniques,
    get_technique,
    techniques_by_difficulty,
    techniques_for_ingredient,
)


class TestAllTechniques:
    def test_returns_list(self):
        result = all_techniques()
        assert isinstance(result, list)

    def test_non_empty(self):
        assert len(all_techniques()) > 0

    def test_all_items_are_techniques(self):
        for technique in all_techniques():
            assert isinstance(technique, Technique)

    def test_each_technique_has_required_fields(self):
        for technique in all_techniques():
            assert technique.name
            assert technique.description
            assert len(technique.steps) > 0
            assert isinstance(technique.difficulty, DifficultyLevel)

    def test_returns_independent_copy(self):
        first = all_techniques()
        first.clear()
        second = all_techniques()
        assert len(second) > 0


class TestGetTechnique:
    def test_returns_technique_by_exact_name(self):
        technique = get_technique("Chiffonade")
        assert technique is not None
        assert technique.name == "Chiffonade"

    def test_case_insensitive(self):
        assert get_technique("chiffonade") is not None
        assert get_technique("CHIFFONADE") is not None

    def test_returns_none_for_unknown(self):
        assert get_technique("Nonexistent Technique XYZ") is None

    def test_all_techniques_retrievable(self):
        for technique in all_techniques():
            found = get_technique(technique.name)
            assert found is not None
            assert found.name == technique.name


class TestTechniquesByDifficulty:
    def test_easy_techniques_exist(self):
        easy = techniques_by_difficulty(DifficultyLevel.EASY)
        assert len(easy) > 0
        for t in easy:
            assert t.difficulty == DifficultyLevel.EASY

    def test_intermediate_techniques_exist(self):
        intermediate = techniques_by_difficulty(DifficultyLevel.INTERMEDIATE)
        assert len(intermediate) > 0
        for t in intermediate:
            assert t.difficulty == DifficultyLevel.INTERMEDIATE

    def test_advanced_techniques_exist(self):
        advanced = techniques_by_difficulty(DifficultyLevel.ADVANCED)
        assert len(advanced) > 0
        for t in advanced:
            assert t.difficulty == DifficultyLevel.ADVANCED

    def test_all_difficulties_partition_catalogue(self):
        easy = techniques_by_difficulty(DifficultyLevel.EASY)
        intermediate = techniques_by_difficulty(DifficultyLevel.INTERMEDIATE)
        advanced = techniques_by_difficulty(DifficultyLevel.ADVANCED)
        assert len(easy) + len(intermediate) + len(advanced) == len(all_techniques())


class TestTechniquesForIngredient:
    def test_basil_returns_results(self):
        results = techniques_for_ingredient("basil")
        assert len(results) > 0

    def test_carrot_returns_results(self):
        results = techniques_for_ingredient("carrot")
        assert len(results) > 0

    def test_partial_match(self):
        # "citrus" should match "citrus slices" and "citrus peel"
        results = techniques_for_ingredient("citrus")
        assert len(results) > 0

    def test_unknown_ingredient_returns_empty(self):
        assert techniques_for_ingredient("unobtanium_xyz") == []

    def test_case_insensitive(self):
        lower = techniques_for_ingredient("basil")
        upper = techniques_for_ingredient("BASIL")
        assert lower == upper


class TestTechniqueSummary:
    def test_summary_contains_name(self):
        technique = get_technique("Chiffonade")
        summary = technique.summary()
        assert "Chiffonade" in summary

    def test_summary_contains_steps(self):
        technique = get_technique("Julienne")
        summary = technique.summary()
        for step in technique.steps:
            assert step in summary

    def test_summary_contains_tools(self):
        technique = get_technique("Julienne")
        summary = technique.summary()
        for tool in technique.tools_required:
            assert tool in summary

    def test_summary_contains_tips(self):
        technique = get_technique("Chiffonade")
        summary = technique.summary()
        for tip in technique.tips:
            assert tip in summary

    def test_str_representation(self):
        technique = get_technique("Chiffonade")
        text = str(technique)
        assert "Chiffonade" in text
        assert "easy" in text
