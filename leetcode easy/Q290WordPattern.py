class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Check if lengths match
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True

# Example Usage:
sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))    # Output: true
print(sol.wordPattern("abba", "dog cat cat fish"))   # Output: false
print(sol.wordPattern("aaaa", "dog cat cat dog"))    # Output: false
