class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0
        left, right = 0, len(height)-1
        while (right - left) >=1:
            h = min(height[left], height[right])
            volume = h * (right-left)
            if volume > largest:
                largest = volume
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1    
        return largest