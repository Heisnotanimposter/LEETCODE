class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove any trailing spaces
        s = s.rstrip()
        # Split the string into words
        words = s.split(' ')
        # Return the length of the last word
        return len(words[-1])

# Examples
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
