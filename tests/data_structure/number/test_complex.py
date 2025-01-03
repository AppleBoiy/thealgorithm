import unittest

from thealgorithm.abc.number import icomplex


class TestIComplex(unittest.TestCase):

    def test_representation_positive_imaginary(self):
        complex_number = icomplex(real=5.0, imag=3.0)
        self.assertEqual(repr(complex_number), "5.0 + 3.0i")

    def test_representation_negative_imaginary(self):
        complex_number = icomplex(real=5.0, imag=-3.0)
        self.assertEqual(repr(complex_number), "5.0 - 3.0i")

    def test_representation_zero_imaginary(self):
        complex_number = icomplex(real=5.0, imag=0.0)
        self.assertEqual(repr(complex_number), "5.0 + 0.0i")

    def test_representation_zero_real_positive_imaginary(self):
        complex_number = icomplex(real=0.0, imag=3.0)
        self.assertEqual(repr(complex_number), "0.0 + 3.0i")

    def test_representation_zero_real_negative_imaginary(self):
        complex_number = icomplex(real=0.0, imag=-3.0)
        self.assertEqual(repr(complex_number), "0.0 - 3.0i")

    def test_representation_zero_real_zero_imaginary(self):
        complex_number = icomplex(real=0.0, imag=0.0)
        self.assertEqual(repr(complex_number), "0.0 + 0.0i")

    def test_default_values_real_and_imaginary(self):
        complex_number = icomplex()
        self.assertEqual(complex_number.real, 0.0)
        self.assertEqual(complex_number.imag, 0.0)
        self.assertEqual(repr(complex_number), "0.0 + 0.0i")

    def test_missing_real_value_provided_imaginary(self):
        complex_number = icomplex(imag=5.0)
        self.assertEqual(complex_number.real, 0.0)
        self.assertEqual(complex_number.imag, 5.0)
        self.assertEqual(repr(complex_number), "0.0 + 5.0i")

    def test_missing_imaginary_value_provided_real(self):
        complex_number = icomplex(real=7.0)
        self.assertEqual(complex_number.real, 7.0)
        self.assertEqual(complex_number.imag, 0.0)
        self.assertEqual(repr(complex_number), "7.0 + 0.0i")

    def test_provide_both_real_and_imaginary(self):
        complex_number = icomplex(real=-4.5, imag=6.7)
        self.assertEqual(complex_number.real, -4.5)
        self.assertEqual(complex_number.imag, 6.7)
        self.assertEqual(repr(complex_number), "-4.5 + 6.7i")


class TestIComplexExtend(unittest.TestCase):

    def test_representation(self):
        z = icomplex(3, -4)
        self.assertEqual(repr(z), "3.0 - 4.0i")

    def test_addition(self):
        z1 = icomplex(3, 4)
        z2 = icomplex(1, -2)
        result = z1 + z2
        expected = icomplex(4, 2)
        self.assertEqual(result, expected)

    def test_subtraction(self):
        z1 = icomplex(5, 6)
        z2 = icomplex(3, 2)
        result = z1 - z2
        expected = icomplex(2, 4)
        self.assertEqual(result, expected)

    def test_multiplication(self):
        z1 = icomplex(1, 2)
        z2 = icomplex(3, 4)
        result = z1 * z2
        expected = icomplex(-5, 10)
        self.assertEqual(result, expected)

    def test_division(self):
        z1 = icomplex(1, 2)
        z2 = icomplex(3, -4)
        result = z1 / z2
        expected = z1 * icomplex(3, 4) / icomplex(3, 4).__abs__() ** 2
        self.assertAlmostEqual(result.real, expected.real, places=6)
        self.assertAlmostEqual(result.imag, expected.imag, places=6)

    def test_equality(self):
        z1 = icomplex(2, 3)
        z2 = icomplex(2, 3)
        z3 = icomplex(1, -1)
        self.assertTrue(z1 == z2)
        self.assertFalse(z1 == z3)

    def test_inequality(self):
        z1 = icomplex(5, 7)
        z2 = icomplex(3, 4)
        z3 = icomplex(5, 7)
        self.assertTrue(z1 != z2)
        self.assertFalse(z1 != z3)

    def test_negation(self):
        z = icomplex(3, -4)
        result = -z
        expected = icomplex(-3, 4)
        self.assertEqual(result, expected)

    def test_abs(self):
        z = icomplex(3, 4)
        self.assertEqual(abs(z), 5)

    def test_float_conversion(self):
        z = icomplex(7.5, -2.3)
        self.assertEqual(float(z), 7.5)

    def test_int_conversion(self):
        z = icomplex(8.4, 3.1)
        self.assertEqual(int(z), 8)

    def test_hash(self):
        z1 = icomplex(3, -4)
        z2 = icomplex(3, -4)
        z3 = icomplex(5, 6)
        self.assertEqual(hash(z1), hash(z2))
        self.assertNotEqual(hash(z1), hash(z3))

    def test_boolean_true(self):
        z = icomplex(3, 0)
        self.assertTrue(bool(z))

    def test_boolean_false(self):
        z = icomplex(0, 0)
        self.assertFalse(bool(z))

    def test_comparison_operators(self):
        z1 = icomplex(1, 2)
        z2 = icomplex(2, 3)
        z3 = icomplex(1, 3)
        self.assertTrue(z1 < z2)
        self.assertTrue(z1 <= z3)
        self.assertTrue(z2 > z1)
        self.assertTrue(z2 >= z3)
        self.assertFalse(z1 > z2)
        self.assertFalse(z2 < z1)
