class Solution:
    def reverse(self, x: int) -> int:
        scale = 1
        if x < 0:
            scale = -1
        reversed_x = int(str(abs(x))[::-1]) * scale
        
        if -2**31 <= reversed_x <= 2**31 - 1:
            return reversed_x
            
        return 0