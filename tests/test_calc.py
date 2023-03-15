import unittest
from math import sqrt, log, pow

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

class TestFunctions(unittest.TestCase):
    
    def test_sqrt(self):
        self.assertAlmostEqual(sqrt(4), 2.0)
        self.assertAlmostEqual(sqrt(2), 1.41421356)
        self.assertAlmostEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(0.25), 0.5)
    
    def test_fact(self):
        self.assertEqual(fact(0), 1)
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(2), 2)
        self.assertEqual(fact(3), 6)
        self.assertEqual(fact(4), 24)
        
    def test_log(self):
        self.assertAlmostEqual(log(1), 0.0)
        self.assertAlmostEqual(log(2), 0.69314718)
        self.assertAlmostEqual(log(10), 2.30258509)
        self.assertAlmostEqual(log(100), 4.60517019)
    
    def test_power(self):
        self.assertAlmostEqual(pow(2, 3), 8)
        self.assertAlmostEqual(pow(2, 0), 1)
        self.assertAlmostEqual(pow(0, 2), 0)
        self.assertAlmostEqual(pow(2, -1), 0.5)

if __name__ == '__main__':
    unittest.main()
