# live->dead: (1->2)
# 1. fewer than 2 live neighbors 
# 2. more than 3 live neighbors
# live->live: 2 or 3 live neighbors (1->1)
# dead->live: 3 live neighbors (0->3)

# (1) live: 1
# (2) dead: 0
# (3) live->dead: 2
# (4) dead->live: 3
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # 8个方向的偏量
        neighbors = [(1, 0), (1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (-1, 1), (1, -1)]
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for x, y in neighbors:
                    next_r, next_c = r+x, c+y
                    if 0<=next_r<m and 0<=next_c<n:
                        if board[next_r][next_c]==1 or board[next_r][next_c]==2:
                            live_neighbors+=1

                if board[r][c]==1: # live cell
                    if live_neighbors<2 or live_neighbors>3:
                        board[r][c] = 2 # live->dead
                else: # dead cell
                    if live_neighbors==3:  # dead->live
                        board[r][c] = 3
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==3:
                    board[i][j]=1
                elif board[i][j]==2:
                    board[i][j]=0


        