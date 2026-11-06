import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_int_input_area(self):
        res = area(12,10)
        self.assertEqual(res, 120)

    def test_float_one_input_area(self):
        res = area(6.8,10)
        self.assertEqual(res, 68.0)
    
    def test_float_all_input_area(self):
        res = area(6.8,69.564)
        self.assertEqual(res, 473.0352)

    def test_zero_value_area(self):
        with self.assertRaises(ValueError):
            area(0,3)

    def test_negative_value_area(self):
        with self.assertRaises(ValueError):
            area(-10,10)

    def test_string_first_value_area(self):
        with self.assertRaises(TypeError):
            area("5",10)
    
    def test_string_second_value_area(self):
        with self.assertRaises(TypeError):
            area(10,"5")

    def test_string_all_input_area(self):
        with self.assertRaises(TypeError):
            area("5","5")

    def test_big_input_area(self):
        number1=10**10000
        number2=20**10000
        expected=number1*number2
        res = area(number1,number2)
        self.assertEqual(res, expected)



    def test_int_input_perimeter(self):
        res = perimeter(12,10)
        self.assertEqual(res, 44)

    def test_float_one_input_perimeter(self):
        res = perimeter(6.8,10)
        self.assertEqual(res, 33.6)
    
    def test_float_all_input_perimeter(self):
        res = perimeter(6.8,69.564)
        self.assertEqual(res, 152.728)

    def test_zero_value_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0,3)
        
    def test_negative_value_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-10,10)

    def test_string_first_value_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5",10)
    
    def test_string_second_value_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(10,"5")

    def test_string_all_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5","5")

    def test_big_input_perimeter(self):
        number1=10**10000
        number2=20**10000
        expected = 2 * (number1 + number2)
        res = perimeter(number1,number2)
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()