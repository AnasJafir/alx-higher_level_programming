import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_update(self):
        # Test update method
        s = Square(2, 3, 4, 5)
        s.update(6, 7, 8, 9)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 8)
        self.assertEqual(s.y, 9)

    def test_to_dictionary(self):
        # Test to_dictionary method
        s = Square(2, 3, 4, 5)
        self.assertEqual(
            s.to_dictionary(), {'id': 5, 'x': 3, 'size': 2, 'y': 4}
            )


if __name__ == '__main__':
    unittest.main()
