import unittest
from math_quiz import random_integer, random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if random operator generated is one of the specified operators
        operators = ['+', '-', '*']
        for _ in range(1000):  
            op = random_operator()
            self.assertTrue(op in operators) 
        

    def test_perform_operation(self):
            # Test cases for perform_operation function
            test_cases = [
                (5, 2, '+', '5 + 2', 7), 
                (5, 7, '-', '5 - 7', -2),
                (5, 2, '*', '5 * 2', 10),  
                (10, 5, '+', '10 + 5', 15),
                (7, 3, '-', '7 - 3', 4),
                (55, 89, '-', '55 - 89', -34),
                (672, 378, '+', '672 + 378', 1050),
                (5, 5, '*', '5 * 5', 25),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem_text, answer = perform_operation(num1, num2, operator)
                self.assertEqual(problem_text, expected_problem)
                self.assertEqual(answer, expected_answer)
                


                

if __name__ == "__main__":
    unittest.main()
