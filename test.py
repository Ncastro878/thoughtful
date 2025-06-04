import unittest
from thoughtful import sort  # <- updated to match your filename

class TestSortFunction(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_special_bulky(self):
        self.assertEqual(sort(200, 20, 20, 10), "SPECIAL")

    def test_special_heavy(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_special_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

if __name__ == "__main__":
    unittest.main()

