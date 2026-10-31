# dfs：沿着一条路径不断的探索，直到找完所有的单词或者当前路径无法继续
# 递归三部曲
#（1）dfs参数和返回值的含义：
# - 参数：x为当前格子的行坐标，y为当前格子的纵坐标，index表示当前需要匹配第几个格子
# - 返回值：表示从当前位置出发，能否匹配word[index:
#（2）终止条件：
# - 当前格子不匹配，则直接返回
# - 当前格子匹配，并且已经到达了word的最后一个字符，则返回true
#（3）单层递归的逻辑
# - 遍历四个搜索方向
# - 对于每个相邻的格子检查是否越界，是否已经被当前路径访问过
# - 如果满足条件则继续递归，如果四个方向都无法匹配，则返回
# 注意：定义一个visited来记录是否访问过，并且后续需要回溯

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        visited = [[False]*len(board[0]) for _ in range(len(board))]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(x, y, k):
            if board[x][y] != word[k]:
                return False
            # 匹配成功，并且已经到达word的最后一个节点
            if board[x][y] == word[k] and k==len(word)-1:
                return True
            # 标记当前节点已访问
            visited[x][y] = True
            for i, j in directions:
                next_x, next_y = x+i, y+j
                if next_x<0 or next_y<0 or next_x>=len(board) or next_y>=len(board[0]): # 超出边界
                    continue
                if visited[next_x][next_y]: # 已经访问过了
                    continue
                if not visited[next_x][next_y] and board[next_x][next_y]==word[k+1]:
                    if dfs(next_x, next_y, k+1):
                        return True
            # 撤销访问标记
            visited[x][y] = False
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]: # 当前格子匹配word的第一个字符，因此从当前格子继续执行dfs
                    if dfs(i, j, 0):
                        return True
        return False