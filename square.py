import unittest

def area(a):
    '''
    Принимает :

        a(float): сторону квадрата

    Возвращаемое значение:

        float Площадь квадрата по формуле a^2

    Например:

        area(10) вернёт 100
    '''
    return a * a


def perimeter(a):
    '''
    Принимает :

        a(float): сторону квадрата

    Возвращаемое значение:

        float Периметр квадрата по формуле 4*a

    Например:

        perimeter(10) вернёт 40
    '''
    return 4 * a

class SqueareTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = area(11)
       self.assertEqual(res, 121)
    
    def test_perimeter(self):
        res = perimeter(15)
        self.assertEqual(res, 60)