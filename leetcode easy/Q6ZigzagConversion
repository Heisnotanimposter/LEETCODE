class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        # Fill rows with characters in zigzag order
        for char in s:
            rows[current_row] += char
            # Determine if we need to go up or down
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        # Join all rows to form the final string
        return ''.join(rows)

solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(solution.convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(solution.convert("A", 1))               # Output: "A"
