import os
import time
import requests
from typing import Optional, Dict, Any
from dotenv import load_dotenv

load_dotenv()


class BaseClient:
    """Generic HTTP client with retry logic and session management."""

    def __init__(self, base_url: str = None, timeout: int = None,
                 retry_attempts: int = None, retry_backoff: float = None):
        self.base_url = base_url or os.getenv('BASE_URL', 'https://api.chucknorris.io/api')
        self.timeout = timeout or int(os.getenv('REQUEST_TIMEOUT', '10'))
        self.retry_attempts = retry_attempts or int(os.getenv('RETRY_ATTEMPTS', '3'))
        self.retry_backoff = retry_backoff or float(os.getenv('RETRY_BACKOFF', '0.3'))
        self.session = requests.Session()

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None,
            **kwargs) -> requests.Response:
        """GET request with retry logic."""
        url = f"{self.base_url}{endpoint}"

        for attempt in range(self.retry_attempts):
            try:
                response = self.session.get(
                    url,
                    params=params,
                    timeout=self.timeout,
                    **kwargs
                )
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                if attempt == self.retry_attempts - 1:
                    raise
                wait_time = self.retry_backoff * (2 ** attempt)
                time.sleep(wait_time)

    def close(self):
        """Close the session."""
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()