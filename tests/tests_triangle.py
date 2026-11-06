import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_int_input_area(self):
        res = area(12,10)
        self.assertEqual(res, 60)

    def test_float_one_input_area(self):
        res = area(6.8,10)
        self.assertEqual(res, 34.0)
    
    def test_float_all_input_area(self):
        res = area(6.8,69.564)
        self.assertEqual(res, 236.5176)

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
        with self.assertRaises(OverflowError):
            area(number1,number2)



    def test_int_input_perimeter(self):
        res = perimeter(12,10,23)
        self.assertEqual(res, 45)

    def test_float_one_input_perimeter(self):
        res = perimeter(6.8,10,32)
        self.assertEqual(res, 48.8)
    
    def test_float_all_input_perimeter(self):
        res = perimeter(6.8,69.564,56.78)
        self.assertEqual(res, 133.144)

    def test_zero_value_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(0,3,4)
        
    def test_negative_value_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-10,10,-30)

    def test_string_first_value_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5",10,6)
    
    def test_string_second_value_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(10,"5",6)

    def test_string_third_value_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(10,5,"6")

    def test_string_all_input_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("5","10","6")

    def test_big_input_perimeter(self):
        number1=10**10000
        number2=20**10000
        number3=30**10000
        expected=number1+number2+number3
        res = perimeter(number1,number2,number3)
        self.assertEqual(res, expected)
        
if __name__ == '__main__':
    unittest.main()