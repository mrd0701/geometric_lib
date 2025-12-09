import unittest
import math
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_zero(self):
       res = circle.area(0)
       self.assertEqual(res, 0)

    def test_area(self):
       res = circle.area(10)
       self.assertEqual(res, 100*math.pi)

    def test_perimeter(self):
        res = circle.perimeter(15)
        self.assertEqual(res, 30*math.pi)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = rectangle.area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)
    
    def test_perimeter(self):
        res = rectangle.perimeter(4,5)
        self.assertEqual(res, 18)


class SqueareTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = square.area(0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = square.area(11)
       self.assertEqual(res, 121)
    
    def test_perimeter(self):
        res = square.perimeter(15)
        self.assertEqual(res, 60)


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(10,0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = triangle.area(10,10)
        self.assertEqual(res,50 )
    def test_perimeter(self):
        res = triangle.perimeter(3,4,5)
        self.assertEqual(res,12)


class TriangleTestCase(unittest.TestCase):
    def test_zero(self):
       res = triangle.area(10, 0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = triangle.area(10, 10)
       self.assertEqual(res, 50)
    
    def test_perimeter(self):
        res = triangle.perimeter(4,5,6)
        self.assertEqual(res, 15)