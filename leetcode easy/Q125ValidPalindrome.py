class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Normalize the string by removing non-alphanumeric characters and converting to lowercase
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the normalized string is the same forwards and backwards
        return filtered == filtered[::-1]

# Example Usage:
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(sol.isPalindrome("race a car"))                      # Output: false
print(sol.isPalindrome(" "))                               # Output: true
