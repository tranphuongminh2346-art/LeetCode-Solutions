class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        length = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in s[i:j]:
                    break
                current_len = j - i + 1
                if current_len > length:
                    length = current_len
        return length