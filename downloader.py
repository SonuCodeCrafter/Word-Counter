import requests
from my_logging import Logger
class urlFetcher:
    """
    Fetching the URL Level things
    """

    @staticmethod
    def validate_url(url: str):
        """
        Validating URLS if Urls contain the proper validation
        """

        return url.startswith('https://') and 'wikipedia.org' in url


    @staticmethod 
    def fetch(url: str) -> str: 
        """Fetch the content of a given URL.""" 
        try: 
            Logger.log_start(url) 
            response = requests.get(url, timeout=10) 
            response.raise_for_status() 
            return response.text 
        except requests.exceptions.RequestException as e: 
            Logger.log_failure(url, str(e)) 
            return None
