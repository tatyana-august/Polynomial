import unittest
from Polynomial import Polynomial


class Test_test1(unittest.TestCase):
    def test_TypeError(self):
        self.assertRaises(TypeError, Polynomial, ['a', 'b'])
        self.assertRaises(TypeError, Polynomial, [])
        self.assertRaises(TypeError, Polynomial, ['a', 54])
        self.assertRaises(TypeError, Polynomial.__add__, Polynomial([1, 2]), "s")
        self.assertRaises(TypeError, Polynomial.__mul__, Polynomial([1, 2]), "s")
        self.assertRaises(TypeError, Polynomial.__eq__, Polynomial([1, 2]), "s")

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

    def test_Str(self):
        p = Polynomial([-1, -4, 0])
        self.assertEqual(str(p), "-x2-4x")
        p = Polynomial([-1, -4, -6])
        self.assertEqual(str(p), "-x2-4x-6")
        p = Polynomial([0])
        self.assertEqual(str(p), "0")
        p = Polynomial([0, 0, 0])
        self.assertEqual(str(p), "0")
        p = Polynomial([1, 4, 6])
        self.assertEqual(str(p), "x2+4x+6")
        p = Polynomial([1, 0, 6])
        self.assertEqual(str(p), "x2+6")
        p = Polynomial([-1, 4, -6])
        self.assertEqual(str(p), "-x2+4x-6")

    def test_StrFloat(self):
        p = Polynomial([0.0])
        self.assertEqual(str(p), "0")
        p = Polynomial([0.0, 0.0, 0.0])
        self.assertEqual(str(p), "0")
        p = Polynomial([-1.2, 4.5, -6.8])
        self.assertEqual(str(p), "-1.2x2+4.5x-6.8")
        p = Polynomial([-1.2, 0.0, -6.8])
        self.assertEqual(str(p), "-1.2x2-6.8")

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
