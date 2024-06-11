import unittest
from tasks import find_max


class TestExamples(unittest.TestCase):

# find_max in an array with one, many integer and no integers
    def test_find_max_with_one_integer(self):
        array = [1]

        result = find_max(array)

        self.assertEqual(result, 1)

    def test_find_max_with_many_integers(self):
        array = [3,1,6,8,2,4,5]

        result = find_max(array)

        self.assertEqual(result, 8)

    def test_find_max_with_no_integer(self):
        array = []

        result = find_max(array)

        self.assertEqual(result, 0)

    if __name__ == "__main__":
        unittest.main()

 