class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Trường hợp chuỗi đầu vào rỗng
        if not digits:
            return []
            
        digit_maps = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }

        # Khởi tạo danh sách kết quả chứa một chuỗi rỗng để làm nền tảng ghép chữ
        ans_lst = [""]
        for digit in digits:
            temp = []
            for letter in digit_maps[digit]:
                for combination in ans_lst:
                    temp.append(combination + letter)
            ans_lst = temp
        
        return ans_lst