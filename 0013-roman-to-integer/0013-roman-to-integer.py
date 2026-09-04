class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        
        # Duyệt từ trái sang phải
        for i in range(len(s) - 1):
            curr_val = roman_map[s[i]]
            # Chỉ cần check nếu số hiện tại nhỏ hơn số ngay sau nó thì TRỪ
            if curr_val < roman_map[s[i+1]]:
                total -= curr_val
            else:
                total += curr_val
                
        # Cộng thêm ký tự cuối cùng (ký tự cuối luôn luôn được cộng)
        return total + roman_map[s[-1]]
