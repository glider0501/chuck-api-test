import pytest
from tests.data.joke_payloads import JOKE_CATEGORIES
from utils.assertions import assert_joke_structure


class TestRandomJokes:
    """Tests for random joke endpoints."""

    def test_random_joke_returns_valid_response(self, jokes_client):
        """Test that random joke endpoint returns 200."""
        response = jokes_client.get_random_joke()
        assert response.status_code == 200
    #
    # def test_random_joke_returns_valid_id(self, jokes_client):
    #     """Test that random joke has valid ID."""
    #     response = jokes_client.get_random_joke()
    #     joke = response.json()
    #     assert joke['id'] is not None
    #     assert isinstance(joke['id'], str)
    #     assert len(joke['id']) > 0
    #
    # def test_random_joke_has_value(self, jokes_client):
    #     """Test that random joke has value text."""
    #     response = jokes_client.get_random_joke()
    #     joke = response.json()
    #     assert 'value' in joke
    #     assert isinstance(joke['value'], str)
    #     assert len(joke['value']) > 0
    #
    # def test_random_joke_has_icon_url(self, jokes_client):
    #     """Test that random joke has icon URL."""
    #     response = jokes_client.get_random_joke()
    #     joke = response.json()
    #     assert 'icon_url' in joke
    #     assert isinstance(joke['icon_url'], str)
    #     assert 'http' in joke['icon_url']
    #
    # @pytest.mark.parametrize("category", JOKE_CATEGORIES, ids=lambda c: f"category-{c}")
    # def test_get_random_joke_by_category(self, category, jokes_client):
    #     """Test getting random joke from each category."""
    #     response = jokes_client.get_random_joke(category=category)
    #     assert response.status_code == 200
    #     joke = response.json()
    #     assert joke['value'] is not None
    #     assert isinstance(joke['value'], str)
    #     assert len(joke['value']) > 0
    #
    # @pytest.mark.parametrize("category", JOKE_CATEGORIES, ids=lambda c: f"category-{c}")
    # def test_joke_response_complete(self, category, jokes_client):
    #     """Test complete joke response structure for each category."""
    #     response = jokes_client.get_random_joke(category=category)
    #     joke = response.json()
    #
    #     # Check all required fields
    #     required_fields = ['icon_url', 'id', 'url', 'value']
    #     for field in required_fields:
    #         assert field in joke, f"Missing field: {field}"
    #
    # def test_different_jokes_returned(self, jokes_client):
    #     """Test that multiple calls return different jokes."""
    #     response1 = jokes_client.get_random_joke()
    #     response2 = jokes_client.get_random_joke()
    #
    #     joke1 = response1.json()['id']
    #     joke2 = response2.json()['id']
    #
    #     # Note: This test can occasionally fail if same joke returned twice
    #     # but probability is very low with large joke database
    #     assert joke1 != joke2, "Expected different jokes, got same one twice"


class TestRandomJokesEdgeCases:
    """Edge case tests for random jokes."""

    def test_invalid_category_error(self, jokes_client):
        """Test handling of invalid category."""
        response = jokes_client.get_random_joke(category='invalid-category-xyz')
        # API may return 200 with no result or 404, either is valid error handling
        assert response.status_code in [200, 404]

    def test_special_characters_in_joke(self, jokes_client):
        """Test that jokes with special characters are handled."""
        response = jokes_client.get_random_joke()
        joke = response.json()
        # Just verify it doesn't crash and has value
        assert len(joke['value']) > 0

    def test_multiple_rapid_requests(self, jokes_client):
        """Test handling of multiple rapid requests."""
        for _ in range(5):
            response = jokes_client.get_random_joke()
            assert response.status_code == 200