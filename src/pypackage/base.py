# -*- coding: utf-8 -*-
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

.. code:: python

    import numpy as np

    import pypackage

    x = np.array([1.0, 2.0])
    norm = pypackage.compute_norm(x)
  
"""

import numpy as np


def compute_norm(x: np.ndarray) -> float:
    """Computes the L2-norm of a vector or a matrix.

    Args:
        x: A vector or a matrix.

    Returns:
        A float representing the L2-norm of x.

    Raises:
        ValueError: Error is raise if x is not a numpy array.
    """
    if not isinstance(x, np.ndarray):
        raise ValueError(
            f"Invalid data type for argument x: {type(x)}. Needs to be a numpy array."
        )

    return float(np.sqrt(np.sum(np.square(x))))
