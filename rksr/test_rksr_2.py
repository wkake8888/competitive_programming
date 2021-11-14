import unittest
from work_test2 import rotate_2darr_90_to_left


class TestTwoDimRotation(unittest.TestCase):

    def test_1x0(self):
        arr = [[]]
        self.assertEqual(rotate_2darr_90_to_left(arr), None)

    def test_1x1(self):
        arr = [[1]]
        self.assertEqual(rotate_2darr_90_to_left(arr), [[1]])

    def test_2x2(self):
        arr = [[1, 2], [3, 4]]
        self.assertEqual(rotate_2darr_90_to_left(arr), [[2, 4], [1, 3]])

    def test_two_different_len_arr(self):
        arr = [[1,2], [3, 4, 5]]
        self.assertEqual(rotate_2darr_90_to_left(arr), None)

    def test_string_arr(self):
        arr = [["a", "b"], ["c", "d"]]
        self.assertEqual(rotate_2darr_90_to_left(arr), [["b", "d"], ["a", "c"]])

    def test_string_and_int(self):
        arr = [["1", 2,], ["3", 4]]
        self.assertEqual(rotate_2darr_90_to_left(arr), [[2, 4], ["1", "3"]])

if __name__ == '__main__':
    unittest.main()