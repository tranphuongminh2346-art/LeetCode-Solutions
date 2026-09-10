class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        return self.kSumClosest(nums, 3, target)

    def kSumClosest(self, nums: list[int], k: int, target: int) -> int:
        
        if len(nums) == k:
            return sum(nums)

     
        smallest_sum = sum(nums[:k])
        if smallest_sum >= target:
            return smallest_sum

        largest_sum = sum(nums[-k:])
        if largest_sum <= target:
            return largest_sum

        if k == 1:
            return min(nums, key=lambda x: abs(target - x))

        closest_sum = smallest_sum
        
        for i in range(len(nums) - k + 1):

            if i > 0 and nums[i] == nums[i - 1]:
                continue


            remainder_closest = self.kSumClosest(nums[i + 1:], k - 1, target - nums[i])
            current_sum = nums[i] + remainder_closest


            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum

            if closest_sum == target:
                return target

        return closest_sum