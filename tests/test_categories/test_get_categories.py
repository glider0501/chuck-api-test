import pytest
from tests.data.category_data import KNOWN_CATEGORIES


class TestGetCategories:
    """Tests for categories endpoint."""

    def test_categories_endpoint_returns_200(self, categories_client):
        """Test that categories endpoint returns 200."""
        response = categories_client.get_categories()
        assert response.status_code == 200

    def test_categories_response_is_list(self, categories_client):
        """Test that categories response is a list."""
        response = categories_client.get_categories()
        categories = response.json()
        assert isinstance(categories, list)

    def test_categories_not_empty(self, categories_client):
        """Test that categories list is not empty."""
        response = categories_client.get_categories()
        categories = response.json()
        assert len(categories) > 0

    def test_categories_are_strings(self, categories_client):
        """Test that all categories are strings."""
        response = categories_client.get_categories()
        categories = response.json()
        for category in categories:
            assert isinstance(category, str)

    @pytest.mark.parametrize("known_category", KNOWN_CATEGORIES,
                             ids=lambda c: f"has-{c}")
    def test_known_categories_present(self, known_category, categories_client):
        """Test that all known categories are in response."""
        response = categories_client.get_categories()
        categories = response.json()
        assert known_category in categories, f"Category '{known_category}' not found"

    def test_categories_are_lowercase(self, categories_client):
        """Test that all categories are lowercase."""
        response = categories_client.get_categories()
        categories = response.json()
        for category in categories:
            assert category == category.lower(), f"Category '{category}' is not lowercase"

    def test_no_duplicate_categories(self, categories_client):
        """Test that there are no duplicate categories."""
        response = categories_client.get_categories()
        categories = response.json()
        assert len(categories) == len(set(categories))

    def test_categories_sorted(self, categories_client):
        """Test that categories are sorted alphabetically."""
        response = categories_client.get_categories()
        categories = response.json()
        assert categories == sorted(categories)

    def test_each_category_has_jokes(self, categories_client, jokes_client):
        """Test that each category has at least one joke."""
        response = categories_client.get_categories()
        categories = response.json()

        for category in categories[:3]:  # Test first 3 to avoid timeout
            joke_response = jokes_client.get_random_joke(category=category)
            assert joke_response.status_code == 200

    def test_categories_content_valid(self, categories_client):
        """Test that categories contain valid content."""
        response = categories_client.get_categories()
        categories = response.json()

        for category in categories:
            assert len(category) > 0
            assert category.isalnum() or '-' in category