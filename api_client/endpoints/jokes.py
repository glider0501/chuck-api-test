from requests import Response

from api_client.base_client import BaseClient


class RandomJokesClient(BaseClient):
    """Client for jokes endpoints."""

    def get_random_joke(self, category: str = None) -> Response:
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
