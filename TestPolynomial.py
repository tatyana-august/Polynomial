import unittest
from Polynomial import Polynomial

class Test_test1(unittest.TestCase):

    def test_Constructor(self):

        pol0 = Polynomial([1.0, 2.1, 3.2, 4.3, 5.4, 6.5])
        self.assertEqual(pol0.coeffs, [1.0, 2.1, 3.2, 4.3, 5.4, 6.5])
        self.assertEqual(pol0.degree, 5)

        pol1 = Polynomial([1, 2, 3, 4])
        self.assertEqual(pol1.coeffs, [1, 2, 3,4])
        self.assertEqual(pol1.degree, 3)

        pol2 = Polynomial([123])
        self.assertEqual(pol2.coeffs, [123])
        self.assertEqual(pol2.degree, 0)

        pol3 = Polynomial([0])
        self.assertEqual(pol3.coeffs, [0])
        self.assertEqual(pol3.degree, 0)

        pol4 = Polynomial([])
        self.assertEqual(pol4.coeffs, [0])
        self.assertEqual(pol4.degree, 0)

        pol5 = Polynomial(0)
        self.assertEqual(pol5.coeffs, [0])
        self.assertEqual(pol5.degree, 0)

        pol6 = Polynomial(6.7)
        self.assertEqual(pol6.coeffs, [6.7])
        self.assertEqual(pol6.degree, 0)

        pol7 = Polynomial(234)
        self.assertEqual(pol7.coeffs, [234])
        self.assertEqual(pol7.degree, 0)

    def test_Str(self):

        pol1 = Polynomial([3, 2, 1])
        self.assertEqual(str(pol1), "3x^2+2x+1")

        pol2 = Polynomial([-3, -2, -1])
        self.assertEqual(str(pol2), "-3x^2-2x-1")

        pol3 = Polynomial([0])
        self.assertEqual(str(pol3), "0")

        pol4 = Polynomial([0, 0, 0])
        self.assertEqual(str(pol4), "0")

        pol5 = Polynomial([-9, 0, 8])
        self.assertEqual(str(pol5), "-9x^2+8")

        pol6 = Polynomial([3.3, 2.2, 1.1])
        self.assertEqual(str(pol6), "3.3x^2+2.2x+1.1")

        pol7 = Polynomial([-3.3, -2.3, -1.3])
        self.assertEqual(str(pol7), "-3.3x^2-2.3x-1.3")

        pol8 = Polynomial([0.0])
        self.assertEqual(str(pol8), "0")

        pol9 = Polynomial([0.0, 0.0, 0.0])
        self.assertEqual(str(pol9), "0")

        pol10 = Polynomial([-9.9, 0.0, 8.9])
        self.assertEqual(str(pol10), "-9.9x^2+8.9")

    def test_Neg(self):

        pol1 = Polynomial([13, 17, 18, 19])
        self.assertEqual(str(-pol1), "-13x^3-17x^2-18x-19")

        pol2 = Polynomial([-13, -17, -18, -19])
        self.assertEqual(str(-pol2), "13x^3+17x^2+18x+19")

        pol3 = Polynomial([-13, 17, -18, 19])
        self.assertEqual(str(-pol3), "13x^3-17x^2+18x-19")

        pol4 = Polynomial([-13.7, 17.8, -18.8, 19.7])
        self.assertEqual(str(-pol4), "13.7x^3-17.8x^2+18.8x-19.7")

        pol5 = Polynomial([-13.7, 0, 18.8, 0.0])
        self.assertEqual(str(-pol5), "13.7x^3-18.8x")

    def test_Eq(self):

        pol1 = Polynomial([1, 2, 3, 4])
        pol2 = Polynomial([-9, 0, 8])
        self.assertEqual(pol1, Polynomial([1, 2, 3, 4]))
        self.assertEqual(pol2, Polynomial([-9, 0, 8]))
        self.assertTrue(pol1 == Polynomial([1, 2, 3, 4]))
        self.assertTrue(pol2 == Polynomial([-9, 0, 8]))
        self.assertFalse(pol1 == pol2)

        pol1 = Polynomial([1.6, 2.6, 3.6, 4.6])
        pol2 = Polynomial([-9.6, 0, 8.6])
        self.assertEqual(pol1, Polynomial([1.6, 2.6, 3.6, 4.6]))
        self.assertEqual(pol2, Polynomial([-9.6, 0, 8.6]))
        self.assertTrue(pol1 == Polynomial([1.6, 2.6, 3.6, 4.6]))
        self.assertTrue(pol2 == Polynomial([-9.6, 0, 8.6]))
        self.assertFalse(pol1 == pol2)

    def test_Ne(self):

        pol1 = Polynomial([1, 2, 3, 4])
        pol2 = Polynomial([-9, 0, 8])
        self.assertFalse(pol1 != Polynomial([1, 2, 3, 4]))
        self.assertFalse(pol2 != Polynomial([-9, 0, 8]))
        self.assertTrue(pol1 != pol2)

        pol1 = Polynomial([1.6, 2.6, 3.6, 4.6])
        pol2 = Polynomial([-9.6, 0, 8.6])
        self.assertFalse(pol1 != Polynomial([1.6, 2.6, 3.6, 4.6]))
        self.assertFalse(pol2 != Polynomial([-9.6, 0, 8.6]))
        self.assertTrue(pol1 != pol2)

    def test_Add(self):

        pol1 = Polynomial([1, 2, 3, 4])
        pol2 = Polynomial([9, 7, 8])
        self.assertListEqual((pol1 + pol2).coeffs, [1, 11, 10, 12])
        self.assertListEqual((pol2 + pol1).coeffs, [1, 11, 10, 12])

        pol1 = Polynomial([1, 2, 3, 4])
        pol2 = Polynomial([-9, -7, -8])
        self.assertListEqual((pol1 + pol2).coeffs, [1, -7, -4, -4])
        self.assertListEqual((pol2 + pol1).coeffs, [1, -7, -4, -4])

        pol1 = Polynomial([0, 2, 3, 0])
        pol2 = Polynomial([-9, 0, -8])
        self.assertListEqual((pol1 + pol2).coeffs, [-7, 3, -8])
        self.assertListEqual((pol2 + pol1).coeffs, [-7, 3, -8])

        pol1 = Polynomial([1.6, 2, 3, 4])
        pol2 = Polynomial([9, 7.6, 8])
        self.assertListEqual((pol1 + pol2).coeffs, [1.6, 11, 10.6, 12])
        self.assertListEqual((pol2 + pol1).coeffs, [1.6, 11, 10.6, 12])

        pol1 = Polynomial([1.1, -2.6, 3.5, 4])
        pol2 = Polynomial([9.1, -7.6, -8])
        self.assertListEqual((pol1 + pol2).coeffs, [1.1, 6.5, -4.1, -4])
        self.assertListEqual((pol2 + pol1).coeffs, [1.1, 6.5, -4.1, -4])

        pol1 = Polynomial([0, 2.7, 3.7, 0])
        pol2 = Polynomial([-9.5, 0, -8.5])
        self.assertListEqual((pol1 + pol2).coeffs, [-6.8, 3.7, -8.5])
        self.assertListEqual((pol2 + pol1).coeffs, [-6.8, 3.7, -8.5])


    def test_AddConst(self):

        pol1 = Polynomial([1.3, -2.6, 0, 4])
        constanta = 5
        self.assertListEqual((pol1 + constanta).coeffs, [1.3, -2.6, 0, 9])
        self.assertListEqual((constanta + pol1).coeffs, [1.3, -2.6, 0, 9])

        pol1 = Polynomial([1.3, -2.6, 0, 4])
        constanta = -5
        self.assertListEqual((pol1 + constanta).coeffs, [1.3, -2.6, 0, -1])
        self.assertListEqual((constanta + pol1).coeffs, [1.3, -2.6, 0, -1])

        pol1 = Polynomial([1.3, -2.6, 0, 4])
        constanta = 0.0
        self.assertListEqual((pol1 + constanta).coeffs, [1.3, -2.6, 0, 4])
        self.assertListEqual((constanta + pol1).coeffs, [1.3, -2.6, 0, 4])

        pol1 = Polynomial([1.3, -2.6, 0, 4.2])
        constanta = -5.7
        self.assertListEqual((pol1 + constanta).coeffs, [1.3, -2.6, 0, -1.5])
        self.assertListEqual((constanta + pol1).coeffs, [1.3, -2.6, 0, -1.5])




    def test_Mult(self):
        p = Polynomial([0., 0, 0., -1, 0, 4.5, 0, -6, 9.9])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p * s).coeffs, (s * p).coeffs)
        p = Polynomial([1, -1, 1])
        s = Polynomial([-1, 1])
        self.assertEqual((p * s).coeffs, [-1, 2, -2, 1])

    def test_MultZero(self):
        p = Polynomial([1, -1, 1])
        s = Polynomial([0, 0])
        self.assertEqual((p * s).coeffs, [0])

    def test_MultFloat(self):
        p = Polynomial([1.5, -1.2, 1.0])
        s = Polynomial([-1, 1])
        self.assertEqual((p * s).coeffs, [-1.5, 2.7, -2.2, 1])

    def test_MultConstFloat(self):
        p = Polynomial([1.5, -1.2, 1.0])
        s = 5
        self.assertEqual((p * s).coeffs, [7.5, -6, 5])

    def test_MultConst(self):
        p = Polynomial([5, -1, 1])
        s = 5
        self.assertEqual((s * p).coeffs, [25, -5, 5])

    def test_LeftMultConst(self):
        p = Polynomial([5, -1, 1])
        s = 5
        self.assertEqual((p * s).coeffs, [25, -5, 5])


    def test_Sub(self):
        p = Polynomial([0., 0, 0., -1, 0, 4.5, 0, -6, 9.9])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p - s).coeffs, [-1, 0, 4.5, 0, -7, 5.9])
        self.assertListEqual((s - p).coeffs, [1, 0, -4.5, 0, 7, -5.9])




if __name__ == '__main__':
    unittest.main()
