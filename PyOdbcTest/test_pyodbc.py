import unittest
import pyodbc

class TestPyOdbcTest(unittest.TestCase):
    def test_pyodbc_version(self):
        self.assertEqual("5.2.0", pyodbc.version)

if __name__ == '__main__':
    unittest.main()
