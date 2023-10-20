import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBaseMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_base_with_id(self):
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_create_base_with_default_id(self):
        new = Base()
        self.assertEqual(new.id, 1)

    def test_increment_id_across_instances(self):
        new1 = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_mix_assigned_and_default_ids(self):
        new1 = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_create_base_with_string_id(self):
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_create_base_with_additional_arguments(self):
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_access_private_attribute(self):
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects

    def test_save_to_file_with_None(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Rectangle.save_to_file(None)
            self.assertEqual(mock_stdout.getvalue(), '[]\n')

    def test_save_to_file_with_empty_list(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Rectangle.save_to_file([])
            self.assertEqual(mock_stdout.getvalue(), '[]\n')

    def test_save_to_file_square(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]\n')
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_rectangle(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]\n')
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

