import unittest

from mtime.time_utilities import add_one

class Test1(unittest.TestCase):
    def test_1(self):
        assert add_one(3)==4

if __name__ == "__main__":
    unittest.main()
