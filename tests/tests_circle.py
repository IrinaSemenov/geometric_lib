import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_two_decimal_places_area(self):
        res = area(12)
        self.assertEqual(res, 452.38)

    def test_required_accuracy_area(self):
        res = area(12)
        self.assertEqual(res, 452.3893421169302)

    def test_float_input_area(self):
        res = area(6.8)
        self.assertEqual(res, 145.26724430199204)
    
    def test_zero_radious_area(self):
        with self.assertRaises(ValueError):
            area(0)
        
    def test_negative_radious_area(self):
        with self.assertRaises(ValueError):
            area(-10)

    def test_string_input_area(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_big_input_area(self):
        number=10**10000
        with self.assertRaises(OverflowError):
            area(number)

    def test_two_decimal_places_perimeter(self):
        res = perimeter(12)
        self.assertEqual(res, 75.39)

    def test_required_accuracy_perimeter(self):
        res = perimeter(12)
        self.assertEqual(res, 75.39822368615503)

    def test_float_input_perimeter(self):
        res = perimeter(6.8)
        self.assertEqual(res, 42.725660088821186)

    def test_zero_radious_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0)
        
    def test_negative_radious_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-10)

    def test_string_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5")
    
    def test_big_input_perimetr(self):
        number=10**10000
        with self.assertRaises(OverflowError):
            perimeter(number)

if __name__ == '__main__':
    unittest.main()