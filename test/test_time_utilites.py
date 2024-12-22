import unittest

import numpy as np

from mtime.time_utilities import PTime


class Test1(unittest.TestCase):
    def test_1(self):
        time_1 = np.datetime64("1950-01-01T01:01:05.123456789")
        ptime = PTime("65", 0.123456789)
        assert ptime == time_1


if __name__ == "__main__":
    unittest.main()
