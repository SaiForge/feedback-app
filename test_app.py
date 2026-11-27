import unittest

from app import add_feedback, average_rating


class FeedbackTest(unittest.TestCase):
    def test_add_feedback(self):
        self.assertEqual(add_feedback([], "Asha", 5), 1)

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            add_feedback([], " ", 4)

    def test_bad_rating(self):
        with self.assertRaises(ValueError):
            add_feedback([], "Ravi", 9)

    def test_average(self):
        store = [{"rating": 4}, {"rating": 5}]
        self.assertEqual(average_rating(store), 4.5)

    def test_average_empty(self):
        self.assertEqual(average_rating([]), 0)


if __name__ == "__main__":
    unittest.main()

