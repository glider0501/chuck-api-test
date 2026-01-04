import os

import pytest
import requests
from dotenv import load_dotenv

from api_client import RandomJokesClient, CategoriesClient, SearchJokesClient

load_dotenv()

@pytest.fixture(scope='session')
def base_url():
    """Get base URL from environment."""
    return os.getenv('BASE_URL', 'https://api.chucknorris.io')

@pytest.fixture(scope='function')
def categories_client(base_url):
    """Create categories client for each test."""
    client = CategoriesClient(base_url=base_url)
    yield client
    client.close()

@pytest.fixture(scope='function')
def jokes_client(base_url):
    """Create jokes client for each test."""
    client = RandomJokesClient(base_url=base_url)
    yield client
    client.close()

@pytest.fixture(scope='function')
def search_client(base_url):
    """Create search jokes client for each test."""
    client = SearchJokesClient(base_url=base_url)
    yield client
    client.close()

@pytest.fixture(scope='session')
def http_session():
    """Create HTTP session for the test session."""
    session = requests.Session()
    yield session
    session.close()
