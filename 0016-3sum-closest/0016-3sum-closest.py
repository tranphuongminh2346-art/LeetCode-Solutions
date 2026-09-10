class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Khởi tạo đáp án bằng tổng của 3 phần tử đầu tiên
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j, k = i + 1, n - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == target:
                    return total
                
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                if total < target:
                    j += 1
                else:
                    k -= 1
                    
        return closest_sum
