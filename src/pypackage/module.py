"""A module for computing geometric distances between vectors.
"""

import numpy as np

from pypackage.base import compute_norm


def euclidean_distance(x: np.ndarray, y: np.ndarray):
    """Computes the Euclidean distance between points x and y given in Cartesian coordinates.

    Args:
        x: A vector.
        y: A vector.

    Returns:
        A float representing the Euclidean distance between x and y.
    """
    distance_vector: np.ndarray = x - y
    distance = compute_norm(distance_vector)
    return distance
