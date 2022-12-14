from enum import IntEnum
from sklearn.metrics import pairwise_distances


class DistanceMetric(IntEnum):
    COSINE = 0
    L1 = 1
    L2 = 2

    @staticmethod
    def get_names():
        return [distance.name for distance in DistanceMetric]


def get_distance(type: int, x: list, y: list):
    return pairwise_distances(x, y, DistanceMetric(type).name.lower())
