import os


class CorpusBuilder:
    """
    Class builds corpus in two ways:
    a) to file -> build_corpus_file method - merge files generated from WikipediaScraper to one file - use once -
    after WikipediaScraper launch
    b) to list -> build_corpus - open CORPUS_FILE and read it - use each time you want to test code

    Attributes:
        CORPUS_FILE     Path to final corpus file
    """
    def __init__(self):
        self.CORPUS_FILE = "../result_corpus.txt"

    def build_corpus_file(self):
        print(os.listdir())
        with open(self.CORPUS_FILE, "w") as corpus_file:
            for category in os.listdir('result'):
                with open(f"result/{category}", 'r') as articles:
                    for line in articles.readlines():
                        corpus_file.write(line)

    def build_corpus(self):
        with open(self.CORPUS_FILE, "r") as corpus_file:
            return [article for article in corpus_file.read().splitlines()]