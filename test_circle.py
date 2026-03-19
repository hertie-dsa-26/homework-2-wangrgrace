import unittest
from circle import Circle
import math

class TestCircle(unittest.TestCase):

    def test_perimeter(self):
        c = Circle(5)
        self.assertAlmostEqual(c.perimeter(), 2 * math.pi * 5)

    def test_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), math.pi * 5 ** 2)

if __name__ == '__main__':
    unittest.main()