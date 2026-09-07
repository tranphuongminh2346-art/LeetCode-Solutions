class Solution:
    def intToRoman(self, num: int) -> str:
        # Danh sách các cặp (giá trị, ký hiệu La Mã) sắp xếp giảm dần
        roman_mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
            (1, "I")
        ]
        
        result = []
        
        # Duyệt qua từng cặp giá trị và ký hiệu
        for value, symbol in roman_mapping:
            if num == 0:
                break
            # Tính số lần ký hiệu này xuất hiện (ví dụ 3000 // 1000 = 3 lần 'M')
            count = num // value
            if count > 0:
                result.append(symbol * count)
                num %= value # Lấy phần dư còn lại để tính tiếp
                
        return "".join(result)