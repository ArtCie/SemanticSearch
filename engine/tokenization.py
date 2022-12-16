from enum import IntEnum
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


class TokenizationTypes(IntEnum):
    TFIDF = 0
    BagOfWords = 1
    Ngrams = 2
    Word2Vec = 3

    @staticmethod
    def get_names():
        return [tokenization.name for tokenization in TokenizationTypes]


class Tokenization:
    def __init__(self, type:  TokenizationTypes):
        self.type = type
        self._vectorizer = None

    def fit_transform(self, corpus):
        if self.type == TokenizationTypes.TFIDF:
            self._vectorizer = TfidfVectorizer()
            return self._vectorizer.fit_transform(corpus)
        elif self.type == TokenizationTypes.BagOfWords:
            self._vectorizer = CountVectorizer()
            return self._vectorizer.fit_transform(corpus)
        elif self.type == TokenizationTypes.Ngrams:
            return NotImplementedError
        elif self.type == TokenizationTypes.Word2Vec:
            return NotImplementedError
        else:
            raise Exception("Tokenization type not supported")

    def transform(self, corpus):
        if self.type == TokenizationTypes.TFIDF:
            return self._vectorizer.transform([corpus])
        elif self.type == TokenizationTypes.BagOfWords:
            return self._vectorizer.transform([corpus])
        elif self.type == TokenizationTypes.Ngrams:
            return NotImplementedError
        elif self.type == TokenizationTypes.Word2Vec:
            return NotImplementedError
        else:
            raise Exception("Tokenization type not supported")
