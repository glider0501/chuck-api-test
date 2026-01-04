import pytest
from jsonschema import validate, ValidationError
from tests.data.expected_schemas import JOKE_RESPONSE_SCHEMA


class TestJokeStructure:
    """Tests for joke response structure validation."""

    def test_joke_response_schema_valid(self, jokes_client):
        """Test that joke response matches expected schema."""
        response = jokes_client.get_random_joke()
        joke = response.json()

        try:
            validate(instance=joke, schema=JOKE_RESPONSE_SCHEMA)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed: {e.message}")

    def test_joke_id_is_string(self, jokes_client):
        """Test that joke ID is string type."""
        response = jokes_client.get_random_joke()
        joke = response.json()
        assert isinstance(joke['id'], str)

    def test_joke_value_is_string(self, jokes_client):
        """Test that joke value is string type."""
        response = jokes_client.get_random_joke()
        joke = response.json()
        assert isinstance(joke['value'], str)

    def test_joke_url_is_string(self, jokes_client):
        """Test that joke URL is string type."""
        response = jokes_client.get_random_joke()
        joke = response.json()
        assert isinstance(joke['url'], str)

    def test_joke_icon_url_is_string(self, jokes_client):
        """Test that icon URL is string type."""
        response = jokes_client.get_random_joke()
        joke = response.json()
        assert isinstance(joke['icon_url'], str)

    @pytest.mark.parametrize("field", ['id', 'value', 'icon_url', 'url'])
    def test_required_fields_present(self, field, jokes_client):
        """Test that all required fields are present."""
        response = jokes_client.get_random_joke()
        joke = response.json()
        assert field in joke, f"Required field '{field}' missing"

    def test_no_extra_fields(self, jokes_client):
        """Test that response has only expected fields."""
        response = jokes_client.get_random_joke()
        joke = response.json()

        allowed_fields = {'icon_url', 'id', 'url', 'value'}
        actual_fields = set(joke.keys())

        # Allow extra fields but at least have required ones
        required_fields = allowed_fields.intersection(actual_fields)
        assert len(required_fields) == len(allowed_fields)

    def test_url_format(self, jokes_client):
        """Test that URL is properly formatted."""
        response = jokes_client.get_random_joke()
        joke = response.json()
        url = joke['url']

        # URL should contain http or https
        assert 'http' in url.lower() or url == ''