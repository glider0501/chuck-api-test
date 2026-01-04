import pytest
from jsonschema import validate
from tests.data.expected_schemas import (
    JOKE_RESPONSE_SCHEMA, REQUIRED_FIELDS  # Optional flexible version
)


class TestJokeStructure:
    """/joke structure tests"""

    @pytest.mark.parametrize("field", REQUIRED_FIELDS,
                             ids=lambda f: f"has-{f}")
    def test_field_types_and_presence(self, field, jokes_client):
        """Parametrized: validates type + presence for all 4 core fields."""
        response = jokes_client.get_random_joke()
        joke = response.json()

        assert field in joke, f"Missing required field: {field}"
        assert isinstance(joke[field], str), f"{field} must be string"
        if field == "value":
            assert len(joke[field]) > 20, "Joke too short"
        elif field == "icon_url":
            assert "chuck-norris.png" in joke[field]

    def test_response_structure_comprehensive(self, jokes_client):
        """Single comprehensive structure test."""
        response = jokes_client.get_random_joke()
        joke = response.json()

        validate(instance=joke, schema=JOKE_RESPONSE_SCHEMA)

        assert isinstance(joke["categories"], list), "Categories must be list"
        assert all(isinstance(cat, str) for cat in joke["categories"])

        assert "http" in joke["url"].lower() or not joke["url"]
        assert len(joke["value"]) > 20
        assert set(REQUIRED_FIELDS).issubset(joke.keys())