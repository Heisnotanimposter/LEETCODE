class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s_to_t = {}
        map_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t
                
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s
        
        return True

# Example Usage:
sol = Solution()
print(sol.isIsomorphic("egg", "add"))    # Output: true
print(sol.isIsomorphic("foo", "bar"))    # Output: false
print(sol.isIsomorphic("paper", "title"))# Output: true
