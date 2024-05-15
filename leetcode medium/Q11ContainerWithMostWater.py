class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area and update max_area in one line
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

# Example Usage:
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(sol.maxArea([1,1]))                # Output: 1
