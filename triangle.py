import unittest

def area(a, h): 
    '''
    Принимает :

        a(float): основание треугольника

        р(float): высота треугольника

    Возвращаемое значение:

        float Площадь треугольника по формуле a *h / 2

    Например:

        area(10,12) вернёт 60
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Принимает :

        a(float): 1 сторона треугольника

        b(float): 2 сторона треугольника

        с(float): 3 сторона треугольника

    Возвращаемое значение:

        float Площадь периметр треугольника по формуле a + b + c

    Например:

        perimeter(10,12,13) вернёт 35
    '''
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_zero(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = area(10, 10)
       self.assertEqual(res, 50)
    
    def test_perimeter(self):
        res = perimeter(4,5,6)
        self.assertEqual(res, 15)