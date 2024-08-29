from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        concat_len = word_len * num_words
        s_len = len(s)

        if s_len < concat_len:
            return []
        
        word_count = Counter(words)
        result = []

        for i in range(s_len - concat_len + 1):
            seen_words = defaultdict(int)

            for j in range(num_words):
                word_index = i + j * word_len
                word = s[word_index:word_index + word_len]

                if word not in word_count:
                    break
                seen_words[word] += 1

                if seen_words[word] > word_count[word]:
                    break
            else:
                result.append(i)
        return result
    
sol = Solution()
sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))  # Output: [0, 9]
print(sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))  # Output: []
print(sol.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # Output: [6, 9, 12]
