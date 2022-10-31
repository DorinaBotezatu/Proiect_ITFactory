import unittest

from testare import f

class ExampleUnittests(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(f(5), 10) # assert f(5) == 10
        self.assertEqual(f(100), 200) # assert f(100) == 200
        self.assertEqual(f(55), 110)

    def test_negative(self):
        self.assertEqual(f(-10), -20)
        self.assertEqual(f(-13), -26)

    def test_zero(self):
        self.assertEqual(f(0), 0)

    def test_float(self):
        self.assertAlmostEqual(f(3.14159), 6.28, places=2)


if __name__ == "__main__":
    unittest.main()
