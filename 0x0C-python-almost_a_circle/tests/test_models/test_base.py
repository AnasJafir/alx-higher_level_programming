import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_auto_assign_id(self):
        # Test if Base assigns an ID automatically
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_auto_assign_increment_id(self):
        # Test if Base assigns an ID + 1 of the previous exists
        b = Base()
        b2 = Base()
        self.assertEqual(b2.id, 4)

    def test_save_assigned_id(self):
        # Test if Base saves the ID passed
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        # Test to_json_string with None
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        # Test to_json_string with empty list
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_id(self):
        # Test to_json_string with list containing dictionaries with 'id'
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        # Test from_json_string with None
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        # Test from_json_string with empty string
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_id(self):
        # Test from_json_string with string containing dictionary with 'id'
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
