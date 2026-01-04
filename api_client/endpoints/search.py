from requests import Response

from api_client.base_client import BaseClient


class SearchJokesClient(BaseClient):
    """Client for jokes endpoints."""

    def search(self, query: str) -> Response:
        """Search for jokes by keyword.

        Args:
            query: Search query string

        Returns:
            Response object with results
        """
        endpoint = '/jokes/search'
        params = {'query': query}

        return self.get(endpoint, params=params)