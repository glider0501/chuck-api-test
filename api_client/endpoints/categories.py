from api_client.base_client import BaseClient


class CategoriesClient(BaseClient):
    """Client for categories endpoint."""

    def get_categories(self):
        """Get all available joke categories.

        Returns:
            Response object with list of categories
        """
        endpoint = '/jokes/categories'
        return self.get(endpoint)