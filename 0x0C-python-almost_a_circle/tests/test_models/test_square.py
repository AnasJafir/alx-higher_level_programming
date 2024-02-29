import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        # Test Square initialization
        s1 = Square(1)
        s2 = Square(1, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s3.y, 3)

    def test_init_with_strings(self):
        # Test Square initialization with strings
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_init_with_negatives(self):
        # Test Square initialization with negative values
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_str(self):
        # Test __str__ method
        s = Square(2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (5) 3/4 - 2")

    def test_update(self):
        # Test update method
        s = Square(2, 3, 4)
        s.update(5, 6, 7, 8)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

    def test_to_dictionary(self):
        # Test to_dictionary method
        s = Square(2, 3, 4, 5)
        self.assertEqual(
            s.to_dictionary(), {'id': 5, 'x': 3, 'size': 2, 'y': 4}
            )


if __name__ == '__main__':
    unittest.main()
