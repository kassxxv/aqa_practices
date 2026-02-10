import unittest
from lesson_12.homeworks import *

class TestHomeworks(unittest.TestCase):
    def test_calculate_sum_positive(self):
        self.assertEqual(calculate_sum_of_elements_in_array(['1,2,3', '10,20']), [6, 30])

    def test_calculate_sum_value_error(self):
        with self.assertRaises(ValueError):
            calculate_sum_of_elements_in_array(['1,2,abc'])

    def test_student_initialization(self):
        s = Student('Filip', 'Fylyp', 18, 84.4)
        self.assertEqual(s.name, 'Filip')
        self.assertEqual(s.avr_score, 84.4)

    def test_student_change_score(self):
        s = Student('Test', 'User', 20, 70.0)
        s.change_score(95.5)
        self.assertEqual(s.avr_score, 95.5)

    def test_longest_word_standard(self):
        words = ['QA', 'Automation', 'Python']
        word, length = longest_word_in_a_list(words)
        self.assertEqual(word, 'Automation')
        self.assertEqual(length, 10)

    def test_longest_word_empty_list(self):
        self.assertEqual(longest_word_in_a_list([]), ("", 0))

    def test_longest_word_single_element(self):
        self.assertEqual(longest_word_in_a_list(['Hello']), ('Hello', 5))

    def test_square_area(self):
        sq = Square(10)
        self.assertEqual(sq.get_area(), 100)

    def test_square_perimeter(self):
        sq = Square(5)
        self.assertEqual(sq.get_perimeter(), 20)

    def test_circle_area(self):
        c = Circle(10)
        self.assertAlmostEqual(c.get_area(), 314.0)

    def test_is_circle(self):
        c = Circle(5)
        self.assertEqual(c.name, "Коло")


if __name__ == '__main__':
    unittest.main()