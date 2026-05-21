"""Tests for the plating module."""

import pytest

from garnish import (
    PlatingGuide,
    PlatingZone,
    all_guides,
    get_guide,
    guides_by_garnish,
    guides_by_zone,
)


class TestAllGuides:
    def test_returns_list(self):
        result = all_guides()
        assert isinstance(result, list)

    def test_non_empty(self):
        assert len(all_guides()) > 0

    def test_all_items_are_plating_guides(self):
        for guide in all_guides():
            assert isinstance(guide, PlatingGuide)

    def test_each_guide_has_required_fields(self):
        for guide in all_guides():
            assert guide.dish_name
            assert guide.description
            assert len(guide.elements) > 0

    def test_returns_independent_copy(self):
        first = all_guides()
        first.clear()
        second = all_guides()
        assert len(second) > 0


class TestGetGuide:
    def test_returns_guide_by_exact_name(self):
        guide = get_guide("Pan-Seared Salmon Fillet")
        assert guide is not None
        assert guide.dish_name == "Pan-Seared Salmon Fillet"

    def test_case_insensitive(self):
        assert get_guide("pan-seared salmon fillet") is not None
        assert get_guide("PAN-SEARED SALMON FILLET") is not None

    def test_returns_none_for_unknown(self):
        assert get_guide("Nonexistent Dish XYZ") is None

    def test_all_guides_retrievable(self):
        for guide in all_guides():
            found = get_guide(guide.dish_name)
            assert found is not None
            assert found.dish_name == guide.dish_name


class TestGuidesByGarnish:
    def test_citrus_twist_appears_in_guides(self):
        results = guides_by_garnish("Citrus Twist")
        assert len(results) > 0

    def test_case_insensitive(self):
        lower = guides_by_garnish("citrus twist")
        upper = guides_by_garnish("CITRUS TWIST")
        assert lower == upper

    def test_partial_match(self):
        # "citrus" should match "Citrus Twist" and "Dehydrated Citrus Wheel"
        results = guides_by_garnish("citrus")
        assert len(results) > 0

    def test_unknown_garnish_returns_empty(self):
        assert guides_by_garnish("Nonexistent Garnish XYZ") == []


class TestGuidesByZone:
    def test_top_zone_has_guides(self):
        results = guides_by_zone(PlatingZone.TOP)
        assert len(results) > 0
        for guide in results:
            zones = [el.zone for el in guide.elements]
            assert PlatingZone.TOP in zones

    def test_rim_zone_has_guides(self):
        results = guides_by_zone(PlatingZone.RIM)
        assert len(results) > 0
        for guide in results:
            zones = [el.zone for el in guide.elements]
            assert PlatingZone.RIM in zones

    def test_center_zone_has_guides(self):
        results = guides_by_zone(PlatingZone.CENTER)
        assert len(results) > 0
        for guide in results:
            zones = [el.zone for el in guide.elements]
            assert PlatingZone.CENTER in zones


class TestPlatingSummary:
    def test_summary_contains_dish_name(self):
        guide = get_guide("Pan-Seared Salmon Fillet")
        summary = guide.summary()
        assert "Pan-Seared Salmon Fillet" in summary

    def test_summary_contains_elements(self):
        guide = get_guide("Pan-Seared Salmon Fillet")
        summary = guide.summary()
        for element in guide.elements:
            assert element.garnish_name in summary

    def test_summary_contains_color_notes(self):
        guide = get_guide("Chocolate Fondant with Vanilla Ice Cream")
        summary = guide.summary()
        assert guide.color_notes in summary

    def test_summary_contains_general_tips(self):
        guide = get_guide("Pan-Seared Salmon Fillet")
        summary = guide.summary()
        for tip in guide.general_tips:
            assert tip in summary

    def test_str_representation(self):
        guide = get_guide("Mezze Platter")
        text = str(guide)
        assert "Mezze Platter" in text
