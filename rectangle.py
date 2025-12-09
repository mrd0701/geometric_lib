import unittest

def area(a, b): 
    '''
    Принимает : 

        a(float): 1 сторону прямоугольника

        b(float): 2 сторону прямоугольника

    Возвращаемое значение:

        float Площадь прямоугольника по формуле a * b

    Например:

        area(10,12) вернёт 120
    '''
    return a * b 

def perimeter(a, b): 
    '''
    Принимает :

        a(float): 1 сторону прямоугольника

        b(float): 2 сторону прямоугольника

    Возвращаемое значение:

        float Периметр прямоугольника по формуле 2*(a + b)

    Например:

        perimeter(10,12) вернёт 44
    '''
    return 2*(a + b) 

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)
    
    def test_perimeter(self):
        res = perimeter(4,5)
        self.assertEqual(res, 18)

