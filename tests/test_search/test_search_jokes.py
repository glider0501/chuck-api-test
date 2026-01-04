import pytest

from tests.data.category_data import SAMPLE_CATEGORIES


class TestSearchJokes:
    """/search endpoint tests."""

    @pytest.mark.parametrize("query,min_results", [
        ("chuck", 10),
        ("norris", 10),
        ("fight", 5),
        ("computer", 3),
        ("xyzabc123", 0),
    ], ids=SAMPLE_CATEGORIES)
    def test_search_endpoint(self, search_client, query, min_results):
        """Parametrized: status, structure, results validation."""
        response = search_client.search(query=query)

        assert response.status_code == 200
        data = response.json()

        assert 'total' in data and isinstance(data['total'], int)
        assert 'result' in data and isinstance(data['result'], list)
        assert len(data['result']) <= data['total']
        assert data['total'] >= min_results

        if data['result']:
            joke = data['result'][0]
            assert all(key in joke for key in ['id', 'value', 'icon_url'])
