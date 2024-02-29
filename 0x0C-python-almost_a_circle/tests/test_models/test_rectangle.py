import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test area calculation
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        # Test display method
        r = Rectangle(2, 3)
        # Since it's printing, we can't directly test output
        self.assertEqual(r.display(), None)

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
