class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each element
        index_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            if num in index_map:
                # Check if the previous index is within k distance
                if i - index_map[num] <= k:
                    return True
            # Update the last seen index of the current element
            index_map[num] = i
        
        # If no such pair is found, return False
        return False

# Example Usage:
sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: true
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: true
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: false
