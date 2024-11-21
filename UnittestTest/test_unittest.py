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
        self.assertEqual([], list())
        self.assertEqual({'a','b','c'}, set("abc"))
        self.assertEqual({}, dict())

    def test_assertNotEqual(self):
        self.assertNotEqual(True, bool())
        self.assertNotEqual({}, set())



if __name__ == '__main__': 
    unittest.main()