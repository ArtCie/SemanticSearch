from math import fabs

from engine.tokenization import Tokenization, TokenizationTypes
from engine.semantic_analyze import Semantic, SemanticTypes
from engine.distance import DistanceMetric, get_distance
import numpy as np


class ModelManager:
    def __init__(self, corpus):
        self._corpus = corpus
        self._tokenization = None
        self._semantic = None
        self._model = None

    def create_model(self, tokenization: TokenizationTypes, semantic: SemanticTypes):
        self._tokenization = Tokenization(tokenization)
        self._semantic = Semantic(semantic)
        corpus_vectorized = self._tokenization.fit_transform(self._corpus).toarray()
        self._model = self._semantic.fit_transform(corpus_vectorized)

    def transform_text(self, text):
        text_vector = self._tokenization.transform(text).toarray()
        return self._semantic.transform(text_vector)

    def get_n_min_indexes(self, vector: list, n=1):
        vector = np.array(vector)
        vector = vector.flatten()
        return vector.argsort()[:n]

    def search(self, text, distance: DistanceMetric):
        text = self.transform_text(text.lower())
        distances = get_distance(distance, self._model, text)
        responses = []
        for index in self.get_n_min_indexes(distances, 16):
            responses.append(f'{distances[index]} - {self._corpus[index]}')
        return responses
