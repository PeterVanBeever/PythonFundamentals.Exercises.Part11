import unittest

from shapes import Rectangle, Square

class TestShapes(unittest.TestCase):
    def test_rectangle_area(self):
        rect = Rectangle(2, 4)
        self.assertEqual(rect.area(), 8)

    def test_rectangle_perimeter(self):
        rect = Rectangle(2, 4)
        self.assertEqual(rect.perimeter(), 12)

    def test_square_area(self):
        square = Square(8)
        self.assertEqual(square.area(), 64)

    def test_square_perimeter(self):
        square = Square(8)
        self.assertEqual(square.perimeter(), 32)

if __name__ == '__main__':
    unittest.main()
