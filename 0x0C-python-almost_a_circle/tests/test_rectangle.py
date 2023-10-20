#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.rectangle import Rectangle
from models.base import Base

class TestRectangleMethods(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_rectangle_with_default_attributes(self):
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_create_rectangle_with_all_attributes(self):
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_create_multiple_rectangles(self):
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)

    def test_rectangle_is_base_instance(self):
        new = Rectangle(1, 1)
        self.assertTrue(isinstance(new, Base))

    def test_create_rectangle_with_incorrect_amount_of_arguments(self):
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_create_rectangle_with_no_arguments(self):
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_access_private_attributes(self):
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_create_rectangle_with_string_values(self):
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_create_rectangle_with_invalid_values(self):
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_rectangle_area(self):
        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_rectangle_display(self):
        r1 = Rectangle(2, 5)
        expected_output = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_str_representation(self):
        r1 = Rectangle(2, 5, 2, 4)
        expected_output = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(1, 2, 3, 4, 1)
        expected_output = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(r1)
            self.assertEqual(mock_stdout.getvalue(), expected_output)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(type(r1.to_dictionary()))
            self.assertEqual(mock_stdout.getvalue(), "<class 'dict'>\n")

    def test_json_string_conversion(self):
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_output = "[{}]\n".format(dictionary.__str__().replace("'", "\""))
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(json_dictionary)
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_method(self):
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_json_file(self):
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_and_save_json_file(self):
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)
        input_rectangles = [r1, r2]
        Rectangle.save_to_file(input_rectangles)
        output_rectangles = Rectangle.load_from_file()
        for i in range(len(input_rectangles)):
            self.assertEqual(input_rectangles[i].__str__(), output_rectangles[i].__str__())

