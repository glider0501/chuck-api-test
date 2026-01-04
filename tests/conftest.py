import pytest
from api_client import JokesClient, CategoriesClient
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope='session')
def base_url():
    """Get base URL from environment."""
    return os.getenv('BASE_URL', 'https://api.chucknorris.io/api')

@pytest.fixture(scope='function')
def jokes_client(base_url):
    """Create jokes client for each test."""
    client = JokesClient(base_url=base_url)
    yield client
    client.close()

@pytest.fixture(scope='function')
def categories_client(base_url):
    """Create categories client for each test."""
    client = CategoriesClient(base_url=base_url)
    yield client
    client.close()

@pytest.fixture(scope='session')
def http_session():
    """Create HTTP session for the test session."""
    import requests
    session = requests.Session()
    yield session
    session.close()