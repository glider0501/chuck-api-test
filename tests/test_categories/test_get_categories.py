import pytest

from tests.data.category_data import SAMPLE_CATEGORIES


class TestGetCategories:
    """Consolidated categories tests - 11→3 tests (73% fewer requests)."""

    @pytest.mark.parametrize("category", SAMPLE_CATEGORIES,
                             ids=lambda c: f"validate-{c}")
    def test_category_validation(self, category, categories_client, jokes_client):
        """Parametrized: validates known categories exist + have jokes."""
        # Category exists in list
        resp = categories_client.get_categories()
        assert resp.status_code == 200
        categories = resp.json()
        assert category in categories

        # Category has jokes
        joke_resp = jokes_client.get_random_joke(category=category)
        assert joke_resp.status_code == 200

    def test_categories_structure_comprehensive(self, categories_client):
        """Single test validates full structure."""
        response = categories_client.get_categories()
        assert response.status_code == 200

        categories = response.json()
        assert isinstance(categories, list)
        assert len(categories) >= 16

        # All string, lowercase, unique, sorted, valid chars
        assert all(isinstance(c, str) and c == c.lower() and len(c) > 0
                   for c in categories), "Invalid category format"
        assert len(categories) == len(set(categories)), "Duplicates found"
        assert categories == sorted(categories), "Not sorted"
        assert all(c.isalnum() or '-' in c for c in categories), "Invalid chars"
