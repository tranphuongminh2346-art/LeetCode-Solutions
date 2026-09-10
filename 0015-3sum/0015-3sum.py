class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        # 1. Sửa lỗi: dùng .sort() thay vì .sorted()
        nums.sort() 
        
        # Lấy độ dài mảng để tái sử dụng
        n = len(nums) 
        
        # 2. Sửa lỗi chính tả chữ "in"
        for i in range(n - 2): 
            # Tối ưu: Nếu số đầu tiên lớn hơn 0, tổng 3 số không thể bằng 0 nữa
            if nums[i] > 0:
                break
                
            # Bỏ qua các phần tử trùng lặp cho vị trí i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 3. Sửa lỗi: Biến n đã được định nghĩa ở trên
            j, k = i + 1, n - 1 

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Bỏ qua các phần tử trùng lặp cho vị trí j và k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
