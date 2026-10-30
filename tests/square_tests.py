import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_int_input_area(self):
        res = area(12)
        self.assertEqual(res, 144)

    def test_float_input_area(self):
        res = area(6.8)
        self.assertEqual(res, 46.24)

    def test_zero_input_area(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_negative_input_area(self):
        with self.assertRaises(ValueError):
            area(-10)

    def test_string_input_area(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_big_input_area(self):
        number=10**10000
        expected=number**2
        res = area(number)
        self.assertEqual(res, expected)



    def test_int_input_perimeter(self):
        res = perimeter(12)
        self.assertEqual(res, 48)

    def test_float_input_perimeter(self):
        res = perimeter(6.8)
        self.assertEqual(res, 27.2)

    def test_zero_input_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0)
        
    def test_negative_value_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-10)

    def test_string_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5")

    def test_big_input_perimeter(self):
        number=10**10000
        expected = 4*number
        res = perimeter(number)
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()