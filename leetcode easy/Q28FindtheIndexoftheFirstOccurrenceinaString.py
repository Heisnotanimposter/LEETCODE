class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Immediate return conditions for special cases
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1

        # Length of needle
        needle_length = len(needle)
        # Maximum index in haystack where a match is possible
        max_index = len(haystack) - needle_length

        # Check each possible starting position in haystack
        for i in range(max_index + 1):
            # Only compare full needle if the first character matches
            if haystack[i] == needle[0]:
                # Check the entire needle
                if haystack[i:i + needle_length] == needle:
                    return i
        
        return -1

# Examples
solution = Solution()
print(solution.strStr("sadbutsad", "sad"))  # Output: 0
print(solution.strStr("leetcode", "leeto"))  # Output: -1
