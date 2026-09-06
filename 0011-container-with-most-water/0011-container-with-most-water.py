class Solution:
    def maxArea(self, height: List[int]) -> int:
        largest = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            h_left = height[left]
            h_right = height[right]
            
            # Tính diện tích hiện tại
            h = h_left if h_left < h_right else h_right
            volume = h * (right - left)
            if volume > largest:
                largest = volume
            
            # Dịch chuyển và bỏ qua các cột thấp hơn
            if h_left < h_right:
                left += 1
                # Bỏ qua nhanh nếu cột tiếp theo không cao hơn cột cũ
                while left < right and height[left] <= h_left:
                    left += 1
            else:
                right -= 1
                # Bỏ qua nhanh nếu cột tiếp theo không cao hơn cột cũ
                while left < right and height[right] <= h_right:
                    right -= 1
                    
        return largest
