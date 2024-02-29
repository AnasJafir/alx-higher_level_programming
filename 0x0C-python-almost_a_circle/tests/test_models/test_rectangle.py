import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        # Test Rectangle initialization
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)

    def test_init_with_strings(self):
        # Test Rectangle initialization with strings
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_init_with_negatives(self):
        # Test Rectangle initialization with negative values
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        # Test area calculation
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        # Test display method
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)

    def test_str(self):
        # Test __str__ method
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")

    def test_update(self):
        # Test update method
        r = Rectangle(2, 3)
        r.update(5, 4, 5, 6, 7)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)

    def test_to_dictionary(self):
        # Test to_dictionary method
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(
            r.to_dictionary(), {
                'x': 4, 'y': 5, 'id': 6, 'height': 3, 'width': 2
                }
            )


if __name__ == '__main__':
    unittest.main()
