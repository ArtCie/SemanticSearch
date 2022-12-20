from enum import IntEnum
from sklearn.decomposition import TruncatedSVD, PCA, LatentDirichletAllocation


class SemanticTypes(IntEnum):
    PCA = 0
    SVD = 1
    LDiA = 2

    @staticmethod
    def get_names():
        return [semantic.name for semantic in SemanticTypes]


class Semantic:
    def __init__(self, type:  SemanticTypes):
        self.type = type
        self._semantic = None

    def fit_transform(self, corpus):
        if self.type == SemanticTypes.PCA:
            self._semantic = PCA(n_components=2)
            return self._semantic.fit_transform(corpus)
        elif self.type == SemanticTypes.SVD:
            self._semantic = TruncatedSVD(n_components=2)
            return self._semantic.fit_transform(corpus)
        elif self.type == SemanticTypes.LDiA:
            self._semantic = LatentDirichletAllocation(n_components=2)
            return self._semantic.fit_transform(corpus)
        else:
            raise Exception("Semantic type not supported")

    def transform(self, corpus):
        return self._semantic.transform(corpus)