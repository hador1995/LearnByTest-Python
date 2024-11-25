import unittest
import logging

logger = logging.getLogger(__name__)


class TestPatternExpression(unittest.TestCase):
    def test_match_as_switch(self):
        for i in range(10):
            match i:
                case 1:
                    self.assertEqual(1, i)
                case 2:
                    self.assertEqual(2, i)
                case 3 | 4:
                    self.assertGreater(5, i)
                case _:
                    self.assertGreater(10, i)

    def test_match_list(self):
        parse = ["app", "arg1", "arg2"]
        match parse:
            case ["app", *result]:
                self.assertListEqual(["arg1", "arg2"], result)
            case _:
                self.fail()

    def test_match_dict(self):
        parse = {"a": 1, "b": 2, "c": 3}
        match parse:
            case {"b": num, **result}:
                self.assertEqual(2, num)
                self.assertDictEqual({"a": 1, "c": 3}, result)
            case _:
                self.fail()

    def test_match_dataclass(self):
        from dataclasses import dataclass

        @dataclass
        class Programmer:
            name: str
            language: str
            framework: str

        programmer1 = Programmer("Om", "Python", "Django")

        match programmer1:
            case Programmer(name, language, framework):
                self.assertEqual("Om", name)
                self.assertEqual("Python", language)
                self.assertEqual("Django", framework)
            case _:
                self.fail()
