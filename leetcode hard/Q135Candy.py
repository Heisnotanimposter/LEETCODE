class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n  # Start with giving each child one candy

        # First pass: Left to Right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Second pass: Right to Left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

# Example Usage:
sol = Solution()
print(sol.candy([1,0,2]))  # Output: 5
print(sol.candy([1,2,2]))  # Output: 4
