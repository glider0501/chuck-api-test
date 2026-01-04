from api_client.base_client import BaseClient


class JokesClient(BaseClient):
    """Client for jokes endpoints."""

    def get_random_joke(self, category: str = None) -> dict:
        """Get a random Chuck Norris joke.

        Args:
            category: Optional category filter

        Returns:
            Response object
        """
        endpoint = '/jokes/random'
        params = {}

        if category:
            params['category'] = category

        return self.get(endpoint, params=params if params else None)

    def search(self, query: str) -> dict:
        """Search for jokes by keyword.

        Args:
            query: Search query string

        Returns:
            Response object with results
        """
        endpoint = '/jokes/search'
        params = {'query': query}

        return self.get(endpoint, params=params)