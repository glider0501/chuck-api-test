import pytest
from tests.data.joke_payloads import SEARCH_TEST_CASES


class TestSearchJokes:
    """Tests for search functionality."""

    def test_search_returns_200(self, jokes_client):
        """Test that search endpoint returns 200."""
        response = jokes_client.search(query='chuck')
        assert response.status_code == 200

    def test_search_response_has_results(self, jokes_client):
        """Test that search response has results."""
        response = jokes_client.search(query='chuck')
        data = response.json()
        assert 'result' in data

    def test_search_response_has_total(self, jokes_client):
        """Test that search response has total count."""
        response = jokes_client.search(query='chuck')
        data = response.json()
        assert 'total' in data

    def test_search_total_is_int(self, jokes_client):
        """Test that total is integer."""
        response = jokes_client.search(query='chuck')
        data = response.json()
        assert isinstance(data['total'], int)

    def test_search_results_is_list(self, jokes_client):
        """Test that results is a list."""
        response = jokes_client.search(query='chuck')
        data = response.json()
        assert isinstance(data['result'], list)

    def test_search_result_count_matches_total(self, jokes_client):
        """Test that result count matches total."""
        response = jokes_client.search(query='chuck')
        data = response.json()
        assert len(data['result']) <= data['total']

    @pytest.mark.parametrize("test_case", SEARCH_TEST_CASES,
                             ids=lambda tc: tc['id'])
    def test_search_queries(self, test_case, jokes_client):
        """Test various search queries."""
        response = jokes_client.search(query=test_case['query'])
        assert response.status_code == 200

        data = response.json()
        assert 'result' in data
        assert 'total' in data
        assert data['total'] >= test_case['min_results']

    def test_search_case_insensitive(self, jokes_client):
        """Test that search is case insensitive."""
        response_lower = jokes_client.search(query='chuck')
        response_upper = jokes_client.search(query='CHUCK')

        count_lower = response_lower.json()['total']
        count_upper = response_upper.json()['total']

        assert count_lower == count_upper

    def test_search_partial_word_match(self, jokes_client):
        """Test that search finds partial word matches."""
        response = jokes_client.search(query='chuc')
        data = response.json()
        assert data['total'] > 0

    def test_search_whitespace_handling(self, jokes_client):
        """Test search with extra whitespace."""
        response = jokes_client.search(query='  chuck  ')
        assert response.status_code == 200

    def test_search_single_character(self, jokes_client):
        """Test search with single character."""
        response = jokes_client.search(query='a')
        assert response.status_code == 200
        # Single char may return many results or none
        data = response.json()
        assert 'total' in data

    def test_search_result_structure(self, jokes_client):
        """Test that search results have proper structure."""
        response = jokes_client.search(query='norris')
        data = response.json()

        if data['total'] > 0:
            result = data['result'][0]
            assert 'id' in result
            assert 'value' in result
            assert 'icon_url' in result

    def test_search_unicode_characters(self, jokes_client):
        """Test search with unicode characters."""
        response = jokes_client.search(query='café')
        assert response.status_code == 200

    def test_empty_search_results(self, jokes_client):
        """Test search with no results."""
        response = jokes_client.search(query='xyzabc123xyz')
        assert response.status_code == 200
        data = response.json()
        assert data['total'] == 0
        assert len(data['result']) == 0

    def test_search_multiple_results(self, jokes_client):
        """Test search returning multiple results."""
        response = jokes_client.search(query='chuck')
        data = response.json()
        assert data['total'] > 1
        assert len(data['result']) > 0

    def test_search_results_contain_query(self, jokes_client):
        """Test that search results contain the query term."""
        query = 'norris'
        response = jokes_client.search(query=query)
        data = response.json()

        for result in data['result'][:3]:  # Check first 3
            assert query.lower() in result['value'].lower()