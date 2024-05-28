class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not the same, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Initialize a counter for 26 lowercase English letters
        count = [0] * 26
        
        # Count each character in s
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Subtract the count for each character in t
        for char in t:
            count[ord(char) - ord('a')] -= 1
            # If any count goes negative, they are not anagrams
            if count[ord(char) - ord('a')] < 0:
                return False
        
        return True

# Example Usage:
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # Output: true
print(sol.isAnagram("rat", "car"))          # Output: false