class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        
        # Vòng lặp thứ nhất (vị trí i)
        for i in range(n - 3):
            # Bỏ qua phần tử trùng lặp cho vị trí i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Tối ưu hóa nâng cao bằng toán học (Có thể bỏ qua nếu muốn code ngắn gọn)
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break # Tổng 4 số nhỏ nhất hiện tại đã lớn hơn target thì không thể tìm thêm bộ nào nữa
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue # Tổng của số hiện tại với 3 số lớn nhất mảng vẫn nhỏ hơn target thì số i này không dùng được
                
            # Vòng lặp thứ hai (vị trí j)
            for j in range(i + 1, n - 2):
                # Bỏ qua phần tử trùng lặp cho vị trí j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Tối ưu hóa nâng cao tương tự cho j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                
                # Áp dụng Kỹ thuật Hai con trỏ cho 2 số còn lại
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # Bỏ qua các phần tử trùng lặp cho left và right
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return ans