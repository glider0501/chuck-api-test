import pytest
from tests.data.joke_payloads import INVALID_SEARCH_INPUTS


class TestSearchErrors:
    """Tests for search error handling."""

    def test_empty_query_string(self, jokes_client):
        """Test search with empty query."""
        response = jokes_client.search(query='')
        assert response.status_code in [200, 400]

    @pytest.mark.parametrize("invalid_input", INVALID_SEARCH_INPUTS,
                             ids=lambda i: i['description'])
    def test_invalid_search_inputs(self, invalid_input, jokes_client):
        """Test search with invalid inputs."""
        response = jokes_client.search(query=invalid_input['query'])
        # API should either return 200 with empty results or error code
        assert response.status_code in [200, 400, 422]

    def test_very_long_search_query(self, jokes_client):
        """Test search with very long query string."""
        long_query = 'a' * 1000
        response = jokes_client.search(query=long_query)
        assert response.status_code in [200, 400, 414]

    def test_special_characters_search(self, jokes_client):
        """Test search with special characters."""
        response = jokes_client.search(query='!@#$%^&*()')
        assert response.status_code in [200, 400]

    def test_null_byte_search(self, jokes_client):
        """Test search with null byte."""
        response = jokes_client.search(query='test\\x00null')
        assert response.status_code in [200, 400]