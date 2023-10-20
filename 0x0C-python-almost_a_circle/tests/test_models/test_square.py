#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import os
from models.square import Square

class TestSquareMethods(unittest.TestCase):
    def setUp(self):
        Square._Base__nb_objects = 0

    def test_create_square(self):
        """ Test creating a square """
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_create_square_with_all_attrs(self):
        """ Test creating a square with all attributes """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_create_multiple_squares(self):
        """ Test creating multiple squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)

    def test_square_is_base_instance(self):
        """ Test if Square is an instance of Base """
        new = Square(1)
        self.assertIsInstance(new, Square)
        self.assertIsInstance(new, Square._Base__base)

    def test_square_incorrect_amount_of_attrs(self):
        """ Test error raised when creating a square with no arguments """
        with self.assertRaises(TypeError):
            new = Square()

    def test_square_access_private_attrs(self):
        """ Test trying to access private attributes """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_square_validate_attrs(self):
        """ Test trying to pass string values """
        with self.assertRaises(TypeError):
            new = Square("2", 2, 2, 2)

    def test_square_invalid_values(self):
        """ Test trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Square(0)

    def test_square_area(self):
        """ Test the area method """
        new = Square(4)
        self.assertEqual(new.area(), 16)

    def test_square_display(self):
        """ Test the display method """
        r1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new_callable=StringIO) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_square_str(self):
        """ Test the __str__ method """
        r1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4"
        self.assertEqual(r1.__str__(), res)

    def test_square_update(self):
        """ Test the update method """
        s1 = Square(3)
        s1.update(5)
        self.assertEqual(s1.id, 5)

    def test_square_to_dictionary(self):
        """ Test the to_dictionary method """
        s1 = Square(1, 2, 3)
        d = s1.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d['size'], 1)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 3)
        self.assertEqual(d['id'], 1)

    def test_square_json_representation(self):
        """ Test JSON representation of Square """
        s1 = Square(2)
        json_representation = s1.to_json_string([s1.to_dictionary()])
        self.assertEqual(json_representation, '[{"id": 1, "size": 2, "x": 0, "y": 0}]')

    def test_square_load_from_file(self):
        """ Test loading from a JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)
        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()
        self.assertEqual(len(linput), len(loutput))
        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())

    def test_create_from_dict(self):
        """ Test creating a Square from a dictionary """
        d = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1 = Square.create(**d)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

if __name__ == "__main__":
    unittest.main()
