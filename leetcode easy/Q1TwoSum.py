class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store numbers and their indices
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices
                return [num_to_index[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            num_to_index[num] = index

# Example Usage:
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(sol.twoSum([3, 3], 6))          # Output: [0, 1]
