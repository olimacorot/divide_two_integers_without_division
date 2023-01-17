import unittest
from practicing.divide_two_integers_without_division.solution import Solution

class TestDivision(unittest.TestCase):

    def setUp(self) -> None:
        self.__solution = Solution()
        return super().setUp()

    def test_it_should_divide_10_by_3_and_return_3(self):
        dividend = 10
        divisor = 3
        want = 3

        self.assertEqual(want, self.__solution.divide(dividend, divisor))
    
    def test_it_should_divide_7_by_3_and_return_2(self):
        dividend = 7
        divisor = 3
        want = 2

        self.assertEqual(want, self.__solution.divide(dividend, divisor))
    
    def test_it_should_divide_1_by_0_and_return_0(self):
        dividend = 1
        divisor = 0
        want = 0

        self.assertEqual(want, self.__solution.divide(dividend, divisor))
    
    def test_it_should_divide_1_by_1_and_return_1(self):
        dividend = 1
        divisor = 1
        want = 1

        self.assertEqual(want, self.__solution.divide(dividend, divisor))

    def test_it_should_divide__1_by_1_and_return__1(self):
        dividend = -1
        divisor = 1
        want = -1

        self.assertEqual(want, self.__solution.divide(dividend, divisor))

    def test_it_should_divide_120_by__1_and_return__120(self):
        dividend = 120
        divisor = -1
        want = -120

        self.assertEqual(want, self.__solution.divide(dividend, divisor))

    def test_it_should_divide__2147483646_by_1_and_return_2147483646(self):
        dividend = 2147483646
        divisor = -1
        want = -2147483646

        self.assertEqual(want, self.__solution.divide(dividend, divisor))
    
    def test_it_should_divide_2147483647_by_1_and_return_2147483647(self):
        dividend = 2147483647
        divisor = 1
        want = 2147483647

        self.assertEqual(want, self.__solution.divide(dividend, divisor))
    
    def test_it_should_divide__2147483648_by_1_and_return_2147483647(self):
        dividend = -2147483648
        divisor = -1
        want = 2147483647

        self.assertEqual(want, self.__solution.divide(dividend, divisor))

    def test_it_should_divide_2147483647_by_2_and_return_2147483647(self):
        dividend = 2147483647
        divisor = 2
        want = 1073741823

        self.assertEqual(want, self.__solution.divide(dividend, divisor))
    