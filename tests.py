import unittest
from vector import Vector
import utilities

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1=Vector(1.0,-2.0,-2.0)
        self.v2=Vector(3.0,6.0,9.0)
        self.x=utilities.probability()

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        sum= self.v1 + self.v2
        self.assertEqual(getattr(sum,"x"),4.0) #assertEqual is used to test the value of an operation
    
    def test_multiplication(self):
        sum= self.v1 * 2
        self.assertEqual(getattr(sum,"x"),2.0) #assertEqual is used to test the value of an operation
if __name__=="__main__":
    unittest.main()