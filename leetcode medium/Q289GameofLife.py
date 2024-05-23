class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # OLD Board: -2 is dead, -1 is alive.
        # NEW BOARD: NEG is dead, POS is alive.

        
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 0:
                    board[r][c] = -2
                else:
                    board[r][c] = -1


        def get_neighors(r, c):
            n = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1), (0,1)]
            
            alive = 0
            for i, j in n:
                row = r + i
                col = c + j
                if row > -1 and row < rows and col > -1 and col < cols:
                    if abs(board[row][col]) == 1:
                        alive +=1 
            return alive

        for r in range(rows):
            for c in range(cols):
                val = abs(board[r][c])
                count = get_neighors(r,c)

                if val == 1 and count in (2,3): 
                    board[r][c] = abs(board[r][c])

                elif val == 2 and count == 3:
                    board[r][c] = abs(board[r][c])


        for r in range(rows):
            for c in range(cols):
                if board[r][c] < 0:
                    board[r][c] = 0 
                else:
                     board[r][c] = 1