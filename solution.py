class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (dividend == 0 or divisor == 0):
            return 0

        count = 0
        positive = (dividend < 0) is (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        while (dividend >= divisor):
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                count += i
                i <<= 1
                temp <<= 1

        if not positive:
            count = -count

        return min(max(-2147483648, count), 2147483647)