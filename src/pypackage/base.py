import numpy as np


def compute_norm(x: np.ndarray) -> float:
    return float(np.sqrt(np.sum(np.square(x))))
