import concurrent.futures
from downloader import urlFetcher
from word_fetcher import WordFetcher
from my_logging import Logger
class ConcurrentProcessor:
    def __init__(self, n_workers):
        self.n_workers = n_workers

    def _process_url(self, url):
        if not urlFetcher.validate_url(url):
            Logger.log_failure(url, 'Provided url is not correct') 
            return url, 0

        content = urlFetcher.fetch(url)
        word_count = WordFetcher.count_words(content)
        Logger.log_success(url, word_count)

        return url, word_count
    
    def process_urls(self, urls):
        results = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.n_workers) as executor:
            future_to_url = {executor.submit(self._process_url, url):url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    Logger.log_failure(url, str(e)) 
                    results.append((url, 0))

        return results

    


