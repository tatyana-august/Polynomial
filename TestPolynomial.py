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

    def test_AddPos(self):
        p = Polynomial([1, 4, 6, 9])
        s = Polynomial([1, 4, 6])
        self.assertListEqual((p + s).coeffs, [1, 5, 10, 15])
        self.assertListEqual((s + p).coeffs, [1, 5, 10, 15])

    def test_AddPosNeg(self):
        p = Polynomial([-1, 4, -6, 9])
        s = Polynomial([1, 4, 6])
        self.assertListEqual((p + s).coeffs, [-1, 5, -2, 15])
        self.assertListEqual((s + p).coeffs, [-1, 5, -2, 15])

    def test_AddPosNegConst(self):
        p = Polynomial([-1, 4, -6, 9])
        self.assertListEqual((p + 6).coeffs, [-1, 4, -6, 15])
        self.assertListEqual((p - 18).coeffs, [-1, 4, -6, -9])

    def test_AddPosNegNull(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p + s).coeffs, [-1, 0, 4, 0, -5, 13])
        self.assertListEqual((s + p).coeffs, [-1, 0, 4, 0, -5, 13])

    def test_AddZero(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = Polynomial([0, 0, 0])
        self.assertListEqual((p + s).coeffs, [-1, 0, 4, 0, -6, 9])

    def test_AddIntConst(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = 5
        self.assertListEqual((p + s).coeffs, [-1, 0, 4, 0, -6, 14])

    def test_LeftAddIntConst(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = 5
        self.assertListEqual((s + p).coeffs, [-1, 0, 4, 0, -6, 14])

    def test_AddFloatConst(self):
        p = Polynomial([0, 0, 0, -1, 0, 4, 0, -6, 9])
        s = 5.6
        self.assertListEqual((p + s).coeffs, [-1, 0, 4, 0, -6, 14.6])

    def test_AddFloat(self):
        p = Polynomial([0., 0, 0., -1, 0, 4.5, 0, -6, 9.9])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p + s).coeffs, [-1, 0, 4.5, 0, -5, 13.9])
        self.assertListEqual((s + p).coeffs, [-1, 0, 4.5, 0, -5, 13.9])

    def test_Sub(self):
        p = Polynomial([0., 0, 0., -1, 0, 4.5, 0, -6, 9.9])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertListEqual((p - s).coeffs, [-1, 0, 4.5, 0, -7, 5.9])
        self.assertListEqual((s - p).coeffs, [1, 0, -4.5, 0, 7, -5.9])

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



    def test_EqualInt(self):
        p = Polynomial([1, 4, 6])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4])
        self.assertEqual(p, Polynomial([1, 4, 6]))
        self.assertTrue(p == Polynomial([1, 4, 6]))
        self.assertTrue(p != s)
        self.assertFalse(p == s)
        s = Polynomial([0, 0, 0, 0, 0])
        p = 0
        self.assertTrue(p == s)
        p = "a"
        self.assertRaises(TypeError, s.__eq__, p)

    def test_EqualFloat(self):
        p = Polynomial([1.5, 4, 6.7])
        s = Polynomial([0, 0, 0, 0, 0, 1, 4.8])
        self.assertEqual(p, Polynomial([1.5, 4, 6.7]))
        self.assertTrue(p == Polynomial([1.5, 4, 6.7]))
        self.assertTrue(p != s)
        self.assertFalse(p == s)


if __name__ == '__main__':
    unittest.main()
