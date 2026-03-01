from collections import deque

class Solution:
    def solve(self, board):
        if not board:
            return
        
        n = len(board)
        m = len(board[0])
        q = deque()
        
        # Step 1: Add boundary O's to queue
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and board[i][j] == 'O':
                    q.append((i, j))
        
        # Directions
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: Mark safe O's
        while q:
            r, c = q.popleft()
            
            if 0 <= r < n and 0 <= c < m and board[r][c] == 'O':
                board[r][c] = 'T'
                
                for dr, dc in dirs:
                    q.append((r+dr, c+dc))
        
        # Step 3: Flip remaining O to X
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # Step 4: Restore safe cells
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'T':
                    board[i][j] = 'O'