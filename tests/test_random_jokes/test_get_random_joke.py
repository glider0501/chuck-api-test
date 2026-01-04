import random

import pytest
import requests

from tests.data.category_data import INVALID_CATEGORY, SAMPLE_CATEGORIES, KNOWN_CATEGORIES
from tests.data.expected_schemas import REQUIRED_FIELDS


class TestRandomJokes:
    """/random joke tests"""

    @pytest.mark.parametrize("category", [None] + SAMPLE_CATEGORIES,
                             ids=lambda c: f"cat-{c or 'none'}")
    def test_random_joke_complete_response(self, category, jokes_client):
        """Parametrized: full validation across categories + no category."""
        response = jokes_client.get_random_joke(category=category)
        assert response.status_code == 200

        joke = response.json()

        for field in REQUIRED_FIELDS:
            assert field in joke
            assert isinstance(joke[field], str)
            if field == 'value':
                assert len(joke[field]) > 20
            elif field == 'icon_url':
                assert 'http' in joke[field]

        assert isinstance(joke['categories'], list)
        assert joke['id']  # Non-empty ID

    def test_category_validation(self, jokes_client):
        """Test valid/invalid categories"""

        valid = jokes_client.get_random_joke(category=random.choice(KNOWN_CATEGORIES))
        assert valid.status_code == 200

        try:
            jokes_client.get_random_joke(category=INVALID_CATEGORY)
            pytest.fail("Expected 404 for invalid category")
        except requests.exceptions.HTTPError as e:
            assert e.response.status_code == 404
            assert INVALID_CATEGORY in e.response.url

    def test_joke_variability(self, jokes_client):
        """Test different jokes returned across multiple calls."""
        ids = {jokes_client.get_random_joke().json()['id']
               for _ in range(5)}
        assert len(ids) >= 3, "Expected joke variety (got repeats)"

    def test_invalid_category_error(self, jokes_client):
        """Test invalid category returns 404."""
        try:
            jokes_client.get_random_joke(category=INVALID_CATEGORY)
            pytest.fail("Expected 404 for invalid category")
        except requests.exceptions.HTTPError as e:
            assert e.response.status_code == 404
            assert INVALID_CATEGORY in e.response.url
