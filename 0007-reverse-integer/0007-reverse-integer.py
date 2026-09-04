class Solution:
    def reverse(self, x: int) -> int:
        scale = 1
        if x < 0:
            scale = -1
        x = abs(x)
        reversed_x = 0
        while x > 0:
            reversed_x = reversed_x * 10 + x%10
            x//=10
        reversed_x *= scale
        
        if -2**31 <= reversed_x <= 2**31 - 1:
            return reversed_x
            
        return 0