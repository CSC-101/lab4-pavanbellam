import data
import lab4
import unittest

from lab4 import x_coordinates
from lab4 import are_in_positive_quadrant
from lab4 import distance
from lab4 import manhattan_distance
from lab4 import distance_all

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input = [[2,3], [4,5]]
        result = lab4.first_element(input)
        expected = [2,4]
        self.assertEqual(expected, result)
    # Part 2
    def test_second1(self):
        pts = [data.Point(4,1), data.Point(5, 3), data.Point(8, 7)]
        result = x_coordinates(pts)
        expected = [4, 5, 8]
        self.assertEqual(expected, result)

    def test_second2(self):
        pts = [data.Point(4,2), data.Point(5, 4), data.Point(1, 2)]
        result = x_coordinates(pts)
        expected = [4, 5, 1]
        self.assertEqual(expected, result)
    # Part 3
    def test_third1(self):
        pts = [data.Point(69,70), data.Point(-25, 46), data.Point(-69, 72), data.Point(65, -3)]
        result = are_in_positive_quadrant(pts)
        expected = [data.Point(69, 70)]
        self.assertEqual(expected, result)

    def test_third2(self):
        pts = [data.Point(4,0), data.Point(1, 8), data.Point(6, 5), data.Point(3, -3)]
        result = are_in_positive_quadrant(pts)
        expected = [data.Point(4, 0), data.Point(1, 8), data.Point(6, 5)]
        self.assertEqual(expected, result)
    # Part 4
    def test_fourth1(self):
        p1 = data.Point(5, 4)
        p2 = data.Point(10, 0)
        result = distance(p1, p2)
        expected = 3.0
        self.assertEqual(expected, result)

    def test_fourth2(self):
        p1 = data.Point(7, 6)
        p2 = data.Point(2, 3)
        result = distance(p1, p2)
        expected = 4.0
        self.assertEqual(expected, result)
    # Part 5
    def test_fifth1(self):
        p1 = data.Point(7, 6)
        p2 = data.Point(2, 3)
        result = manhattan_distance(p1, p2)
        expected = 8.0
        self.assertEqual(expected, result)

    def test_fifth2(self):
        p1 = data.Point(1, 6)
        p2 = data.Point(2, 11)
        result = manhattan_distance(p1, p2)
        expected = 6.0
        self.assertEqual(expected, result)
    # Part 6
    def test_sixth1(self):
        pts = [data.Point(4,0), data.Point(4, 3), data.Point(6, 8), data.Point(3, -4)]
        result = distance_all(pts)
        expected = [4.0, 5.0, 10.0, 5.0]
        self.assertEqual(expected, result)

    def test_sixth1(self):
        pts = [data.Point(0,3), data.Point(-3, -4), data.Point(4.5, 0), data.Point(-3.6, 0)]
        result = distance_all(pts)
        expected = [3.0, 5.0, 4.5, 3.6]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()