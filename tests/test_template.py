import unittest

import numpy as np

from pypackage.base import compute_norm


class TestBase(unittest.TestCase):
    def test_norm(self):
        # Test towards pre-computed value
        x = np.array([1.0, 2.0, 3.0], dtype=float)
        norm = compute_norm(x)
        result = float(np.sqrt(14.0))

        self.assertIsInstance(norm, float)
        self.assertEqual(norm, result)

    def test_norm_numpy(self):
        # Test towards numpy's implementation
        x = np.array([1.0, 2.0, 3.0], dtype=float)
        norm = compute_norm(x)
        result = float(np.linalg.norm(x))

        self.assertIsInstance(norm, float)
        self.assertEqual(norm, result)


if __name__ == "__main__":
    unittest.main()
