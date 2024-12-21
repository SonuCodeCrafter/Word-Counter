
class WordFetcher:
    "Fetch the Word Count"
    @staticmethod
    def count_words(text):
        "fetch Word Count"
        return 0 if not text else len(text.split())

