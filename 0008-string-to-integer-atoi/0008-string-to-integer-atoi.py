class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Remove leading whitespaces
        s = s.strip()
        if not s:
            return 0
        
        # 2. Determine signedness
        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
            
        # 3. Read digits and terminate immediately on non-digits
        ans = 0
        for i in range(start, len(s)):
            if s[i].isdigit():
                ans = ans * 10 + int(s[i])
            else:
                break # Stop processing immediately
                
        # Apply the tracked sign
        ans *= sign
        
        # 4. Clamp within 32-bit signed integer bounds
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX
            
        return ans