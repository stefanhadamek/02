import unittest
from math_quiz import getRandomIntInIntervall, chooseRandomMathOperator, performOperation


class TestMathGame(unittest.TestCase):

    def test_getRandomIntInIntervall(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getRandomIntInIntervall(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    

    def test_chooseRandomMathOperator(self):
        
        for _ in range(1000):
            rand_op  = chooseRandomMathOperator()
            ops = ["+","-","*"]
            self.assertTrue(rand_op in ops)


    def test_performOperation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (12, 8, '-', '12 - 8', 4),
                (7, 3, '*', '7 * 3', 21),
                (15, 5, '+', '15 + 5', 20),
                (10, 4, '-', '10 - 4', 6),
                (18, 3, '*', '18 * 3', 54),
                (9, 6, '+', '9 + 6', 15),
                (20, 2, '-', '20 - 2', 18),
                (4, 2, '*', '4 * 2', 8),
                (11, 3, '+', '11 + 3', 14)
                
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                statement, output = performOperation(num1,num2,operator)
                self.assertEqual(statement,expected_problem)
                self.assertEqual(output , expected_answer)
                

if __name__ == "__main__":
    unittest.main()
