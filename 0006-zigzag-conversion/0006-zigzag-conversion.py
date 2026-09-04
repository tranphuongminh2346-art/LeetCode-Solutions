class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        res = []
        cycle = 2 * numRows - 2
        
        for r in range(numRows):
            # 1. Lấy nhanh các phần tử chính ở đỉnh/đáy/bước nhảy chuẩn của hàng r
            # Cú pháp s[r::cycle] chạy bằng mã C nguyên bản nên nhanh vô địch
            row_elements = s[r::cycle]
            
            # Nếu là hàng đầu hoặc hàng cuối, chỉ cần lấy bước nhảy chuẩn là đủ
            if r == 0 or r == numRows - 1:
                res.append(row_elements)
            else:
                # 2. Với các hàng ở giữa, cần đan xen phần tử "đi lên" của chữ V
                # Phần tử phụ này nằm ở vị trí s[i + cycle - 2*r]
                extra_elements = s[cycle - r::cycle]
                
                # Trộn xen kẽ hai chuỗi lại với nhau bằng zip
                combined = [a + b for a, b in zip(row_elements, extra_elements)]
                
                # Thêm phần thừa nếu chuỗi chính dài hơn chuỗi phụ
                if len(row_elements) > len(extra_elements):
                    combined.append(row_elements[-1])
                    
                res.append("".join(combined))
                
        return "".join(res)
