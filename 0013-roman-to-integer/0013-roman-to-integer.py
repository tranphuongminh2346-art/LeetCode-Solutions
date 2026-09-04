class Solution:
    def romanToInt(self, s: str) -> int:
        # Thay 6 trường hợp đặc biệt thành chuỗi cộng thuần túy
        s = s.replace("IV", "IIII").replace("IX", "VIIII") \
             .replace("XL", "XXXX").replace("XC", "LXXXX") \
             .replace("CD", "CCCC").replace("CM", "DCCCC")
        
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Hàm sum() chạy bằng mã C tích hợp sẵn nên cực kỳ nhanh
        return sum(roman_map[char] for char in s)
