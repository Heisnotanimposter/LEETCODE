class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index, t_index = 0, 0  # pointers for each string
        while t_index < len(t):
            if s_index < len(s) and s[s_index] == t[t_index]:
                s_index += 1  # move the pointer for s if there's a match
            t_index += 1  # always move the pointer for t
        return s_index == len(s)  # true if all characters in s were found in t in order

# Example Usage:
sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))  # Output: true
print(sol.isSubsequence("axc", "ahbgdc"))  # Output: false
