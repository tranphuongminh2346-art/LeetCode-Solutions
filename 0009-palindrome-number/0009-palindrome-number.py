class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        if x < 0:
            return False
        left = 0
        right = len(xstr) - 1
        while left < right:
            if xstr[left] != xstr[right]:
                return False
            else:
                left +=1
                right -=1
        return True