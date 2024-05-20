class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        result = []

        while top <= bottom and left <= right:
            # Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

# Example Usage:
sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))  # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
