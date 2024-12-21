from dataclasses import dataclass
import logging

@dataclass
class Logger:

    @staticmethod
    def config_logger():
        return logging.basicConfig(
            level=logging.INFO,
            format = '%(asctime)s - %(messages)s',
            handlers=[logging.StreamHandler()]
        )

    @staticmethod
    def start_logging():
        logging.info(f"Start logging download")

    @staticmethod 
    def log_start(url: str): 
        logging.info(f"Starting download: {url}") 
    @staticmethod 
    def log_success(url: str, word_count: int): 
        logging.info(f"Finished {url} with word count: {word_count}") 

    @staticmethod 
    def log_failure(url: str, error: str): 
        logging.error(f"Failed {url} - Error: {error}")

