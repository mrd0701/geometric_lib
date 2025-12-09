import math
import unittest

def area(r):
    '''

    Принимает :

        r(float): радиус круга

    Возвращаемое значение:

        float Площадь круга по формуле pi*r^2

    Например:

        area(10) вернёт 314.1592653589793

    '''
    return math.pi * r * r


def perimeter(r):
    '''

    Принимает :

        r(float): радиус круга

    Возвращаемое значение:

        float Периметр по формуле 2 * pi * r

    Например:

        perimeter(10) вернёт 62.83185307179586

    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = area(10)
       self.assertEqual(res, 100*math.pi)
    
    def test_perimeter(self):
        res = perimeter(15)
        self.assertEqual(res, 30*math.pi)
