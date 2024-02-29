import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_to_json_string_empty(self):
        # Test to_json_string with empty list
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        # Test to_json_string with None
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_empty(self):
        # Test from_json_string with empty string
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        # Test from_json_string with None
        self.assertEqual(Base.from_json_string(None), [])


if __name__ == '__main__':
    unittest.main()
