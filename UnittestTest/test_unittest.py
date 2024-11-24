import unittest
import logging

logger = logging.getLogger(__name__)


class UnittestTest(unittest.TestCase):
    def test_assertTrue(self):
        self.assertTrue(True)

    def test_assertFalse(self):
        self.assertFalse(False)

    def test_assertEqual(self):
        self.assertEqual(False, bool())
        self.assertEqual("", str())
        self.assertEqual(0, int())
        self.assertEqual((1,2), tuple((1,2)))
        self.assertEqual({'a','b','c'}, set("abc"))

    def test_assertNotEqual(self):
        self.assertNotEqual(True, bool())
        self.assertNotEqual({}, set())

    def test_assertRaises(self):
        with self.assertRaises(ZeroDivisionError):
            a = 3
            a /= 0

    def test_assertAlmostEqual(self):
        self.assertAlmostEqual(0.3333333, 1/3) #places=7
        self.assertAlmostEqual(0.33, 1/3, places=2)

    def test_assertIn(self):
        self.assertIn('a', ['a','b','c'])

    def test_assertIsNone(self):
        self.assertIsNone(None, None)

    def test_assertDictEqual(self):
        self.assertDictEqual({}, dict())

    def test_assertListEqual(self):
        self.assertListEqual([], list())
    

if __name__ == '__main__': 
    unittest.main()