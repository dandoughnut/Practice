class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            
            negative = 1
            print('negative', negative)
        result = 0
        dividend, divisor = abs(dividend), abs(divisor)
        
        if divisor == 1:
            result = dividend if negative == 0 else -dividend
            
        else:
            # the clever part
            result = len(range(0, dividend-divisor+1, divisor))
            
            result = result if negative == 0 else -result
        return min(max(-2**31, result), 2**31 - 1) 

# somewhat solved it, but range method smart in terms of saving runtime.