import unittest
from unittest.mock import patch
import logging
import sys

logger = logging.getLogger(__name__)

class UnittestPatchTest(unittest.TestCase):
    def test_patch_builtins_function(self):
        with patch("builtins.print") as mock_print:

            print("Hello world", end="\n");
            args, kwargs = mock_print.call_args
            self.assertEqual(('Hello world',) , args)
            self.assertEqual({'end': '\n'} , kwargs)

            print("print error", file=sys.stderr);
            args, kwargs = mock_print.call_args
            self.assertEqual(('print error',) , args)
            self.assertEqual({'file': sys.stderr} , kwargs)

