import unittest

import numpy as np

from mtime.time_utilities import datetime_to_ptime


class Test1(unittest.TestCase):
    def test_1(self):
        time_1 = np.datetime64("1950-01-01T01:01:05.123456789")
        res = datetime_to_ptime(time_1)
        assert res.w_sec == "3665"
        assert np.isclose(res.f_sec, 0.123456789)


if __name__ == "__main__":
    unittest.main()
