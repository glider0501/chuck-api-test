import pytest
import requests


class TestSearchErrors:
    """Tests API responses (400 or 200)."""

    @pytest.mark.parametrize("case", [
        {"query": "", "status": 400, "desc": "empty"},
        {"query": " " * 50, "status": 200, "desc": "long-whitespace"},
        {"query": "a" * 100, "status": 200, "desc": "long-query"},
        {"query": "!@#$%^&*()<>", "status": 200, "desc": "special-chars"},
        {"query": "xyz123nonexistent", "status": 200, "desc": "no-results"},
    ])
    def test_search_error_cases(self, search_client, case):
        """Validate response status matches expected."""
        try:
            response = search_client.search(query=case["query"])
        except requests.exceptions.HTTPError as e:
            assert case["status"] == 400
            assert e.response.status_code == 400
            assert e.response.url.endswith("query=")
            return

        assert case["status"] == 200
        assert response.status_code == 200

        data = response.json()
        assert isinstance(data["total"], int)
        assert data["total"] == 0
        assert isinstance(data["result"], list)
        assert len(data["result"]) == 0
