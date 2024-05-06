class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string into words (automatically removes excessive whitespace)
        words = s.split()
    
        # Step 2: Reverse the list of words
        words.reverse()
    
        # Step 3: Join the words with a single space
        return ' '.join(words)

# Examples
solution = Solution()
print(solution.reverseWords("the sky is blue"))     # Output: "blue is sky the"
print(solution.reverseWords("  hello world  "))    # Output: "world hello"
print(solution.reverseWords("a good   example"))    # Output: "example good a"
