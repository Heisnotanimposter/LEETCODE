class Solution:
    def threeSum(self, nums):
        nums.sort()  # Sort the array
        result = []
        n = len(nums)
        
        for i in range(n):
            # Skip the same elements to avoid duplicates in the result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers approach to find pairs summing to -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Move left pointer to the right, skipping over duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move right pointer to the left, skipping over duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # We need a larger sum
                else:
                    right -= 1  # We need a smaller sum
        
        return result

# Example Usage:
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(sol.threeSum([0, 1, 1]))              # Output: []
print(sol.threeSum([0, 0, 0]))              # Output: [[0, 0, 0]]