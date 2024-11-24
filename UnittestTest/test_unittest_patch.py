import unittest
from unittest.mock import Mock, patch, mock_open
import logging
import sys

logger = logging.getLogger(__name__)

class UnittestPatchTest(unittest.TestCase):
    def test_patch_builtins_function_print(self):
        with patch("builtins.print") as mock_print:

            print("Hello world", end="\n");
            args, kwargs = mock_print.call_args
            self.assertEqual(('Hello world',) , args)
            self.assertEqual({'end': '\n'} , kwargs)

            print("print error", file=sys.stderr);
            args, kwargs = mock_print.call_args
            self.assertEqual(('print error',) , args)
            self.assertEqual({'file': sys.stderr} , kwargs)

    def test_patch_builtins_function_open_context_manager(self):
        with patch("builtins.open") as mock_open:
            mock_file = Mock()
            mock_file.readlines.return_value = ['a\n', '1\n', 'False\n']                        
            mock_open.return_value.__enter__.return_value= mock_file
            with open("test.txt", "r") as file:
                self.assertListEqual(['a\n', '1\n', 'False\n'], file.readlines())

    def test_patch_builtins_function_open(self):
        with patch("builtins.open") as mock_open:
            mock_file = Mock()
            mock_file.readlines.return_value = ['a\n', '1\n', 'False\n']            
            mock_open.return_value = mock_file            
            file = open("test.txt", "r")
            self.assertListEqual(['a\n', '1\n', 'False\n'], file.readlines())

    def test_patch_builtins_function_mock_open(self):
        with patch("builtins.open", mock_open(read_data="a\n1\nFalse\n") ):

            file = open("test.txt", "r")
            self.assertListEqual(['a\n', '1\n', 'False\n'], file.readlines())

            with open("test.txt", "r") as file:
                self.assertListEqual(['a\n', '1\n', 'False\n'], file.readlines())

if __name__ == "__main__":
    unittest.main()

