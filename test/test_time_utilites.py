import math
import unittest

import numpy as np

from mtime.time_utilities import (
    PTime,
    Units,
    datetime_to_ptime,
    epoch_for_np,
    ptime_to_datetime,
    ptime_to_ticks,
)


class TestUnits(unittest.TestCase):
    def test_conversion(self):
        foo = Units.nano
        assert math.isclose(foo.value * 5, 5e-9)


class TestPtime(unittest.TestCase):
    def test_epoch(self):
        epoch = epoch_for_np("19910521")
        assert epoch == "1991-05-21"

    def test_change_epoch(self):
        ptime = PTime(345600, 0.123, epoch="19910204")
        ptime.change_epoch("19910206")

        assert ptime.epoch == "19910206"
        assert ptime.w_sec == 172800
        assert math.isclose(ptime.f_sec, 0.123)

    def test_to_dict(self):
        ptime = PTime(345600, 0.123, epoch="19910204")
        assert ptime.gtk_format == {"w_sec": 345600, "f_sec": 0.123}

    def test_diff(self):
        ptime1 = PTime(345602, 0.123456789, epoch="19910204")
        ptime2 = PTime(245600, 0.100000001, epoch="19910204")

        diff = ptime1 - ptime2
        # check for accuracy to nearest nanosecond
        assert not math.isclose(diff.f_sec, 0.023456789, abs_tol=1e-10)
        assert math.isclose(diff.f_sec, 0.023456788, abs_tol=1e-10)
        assert diff.w_sec == 100002

    def test_to_ticks(self):
        time1 = PTime(345602, 0.123456789, epoch="19910204")

        res = ptime_to_ticks(time1)
        assert res == 345602123456789


class Test1(unittest.TestCase):
    def test_1(self):
        time_1 = np.datetime64("1950-01-01T01:01:05.123456789")
        res = datetime_to_ptime(time_1)
        assert res.w_sec == 3665
        assert np.isclose(res.f_sec, 0.123456789)

    def test_other_way(self):
        ptime = PTime(3665, 0.123456789)
        res = ptime_to_datetime(ptime)
        assert res == np.datetime64("1950-01-01T01:01:05.123456789")


if __name__ == "__main__":
    unittest.main()
