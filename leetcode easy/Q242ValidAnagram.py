from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not the same, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Count the frequency of each character in both strings
        return Counter(s) == Counter(t)

# Example Usage:
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # Output: true
print(sol.isAnagram("rat", "car"))          # Output: false
