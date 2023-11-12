import unittest
from math_quiz import generate_random_number, choose_random_operator, calculate


class TestMathGame(unittest.TestCase):

    def test_generate_random_number(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_number(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value)

    def test_choose_random_operator(self):
        valid_operatiors = {'+', '-', '*', '/'}
        for _ in range(1000): # Test a large number of times
            operator = choose_random_operator()
            self.assertIn(operator, valid_operatiors)

    def test_calculate(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 2, '-', '7 - 2', 5),
            (4, 3, '*', '4 * 3', 12),
            (8, 2, '/', '8 / 2', 4)
        ]

        for operand1, operand2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate(operand1, operand2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
