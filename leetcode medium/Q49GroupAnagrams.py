from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict of list
        anagrams = defaultdict(list)
        
        # Iterate through each string in the list
        for s in strs:
            # Sort the string to get the key
            key = ''.join(sorted(s))
            # Append the original string to the list corresponding to the key
            anagrams[key].append(s)
        
        # Return the values of the dictionary
        return list(anagrams.values())