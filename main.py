from concurrent_handler import ConcurrentProcessor
from writer import ResultWriter
from my_logging import Logger
def main():
    Logger.config_logger()

    print('Enter Wikipedia URLS')
    user_input = input(">")
    wikipedia_urls = [url.strip() for url in user_input.split(',') if url.strip()]
    
    if wikipedia_urls and isinstance(wikipedia_urls, list):

        processor = ConcurrentProcessor(n_workers=3)
        results = processor.process_urls(wikipedia_urls)

        ResultWriter.write_to_file(results)
    else:
        raise Exception("No Valid URL is provided")
        exit(1)

if __name__ == "__main__":
    main()