class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Normalize k to be less than n

        # Helper function to reverse elements from index start to end (inclusive)
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the whole array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the rest
        reverse(k, n - 1)

# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol.rotate(nums, k)
    print(nums)  # Output: [5,6,7,1,2,3,4]