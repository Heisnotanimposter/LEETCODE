class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                # Move the left pointer to the right of the last occurrence of s[right]
                left = char_index_map[s[right]] + 1
            
            # Update the last occurrence of the character
            char_index_map[s[right]] = right
            
            # Calculate the current length of the substring and update max_length
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Example Usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3
