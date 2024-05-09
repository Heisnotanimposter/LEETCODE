class Solution:
    def fullJustify(self, words, maxWidth):
        res, current_line, num_of_letters = [], [], 0

        for word in words:
            # Check if adding the next word exceeds the width
            if num_of_letters + len(word) + len(current_line) > maxWidth:
                # Time to justify the line
                for i in range(maxWidth - num_of_letters):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                res.append(''.join(current_line))
                current_line, num_of_letters = [], 0
            
            # Add current word into the line and update the letter count
            current_line.append(word)
            num_of_letters += len(word)

        # Last line - left justified
        res.append(' '.join(current_line).ljust(maxWidth))
        return res

# Examples
solution = Solution()
example1 = ["This", "is", "an", "example", "of", "text", "justification."]
print(solution.fullJustify(example1, 16))

example2 = ["What","must","be","acknowledgment","shall","be"]
print(solution.fullJustify(example2, 16))

example3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
print(solution.fullJustify(example3, 20))
