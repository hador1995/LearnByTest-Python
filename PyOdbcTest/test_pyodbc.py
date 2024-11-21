import unittest
from unittest.mock import patch
import pyodbc
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='tests.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(message)s', filemode="w")

class TestPyOdbcTest(unittest.TestCase):
    def test_pyodbc_version(self):
        logger.info(f"PyOdbc version: {pyodbc.version}")
        with patch('pyodbc.version', new="x.y.z"):
            self.assertEqual("x.y.z", pyodbc.version)

    def test_pyodbc_dataSources(self):
        logger.info(f"PyOdbc dataSources: {pyodbc.dataSources()}")
        with patch('pyodbc.dataSources') as mock_dataSources:
            mock_dataSources.return_value={'name':'driver'}
            self.assertEqual({'name':'driver'}, pyodbc.dataSources())

    def test_pyodbc_drivers(self):
        logger.info(f"PyOdbc drivers: {pyodbc.drivers()}")
        with patch('pyodbc.drivers') as mock_drivers:
            mock_drivers.return_value=['driver1','driver2']
            self.assertEqual(['driver1','driver2'], pyodbc.drivers())


if __name__ == '__main__': 
    unittest.main()

