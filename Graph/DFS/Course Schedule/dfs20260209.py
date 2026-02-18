# 思路：只要遇到了环则直接返回False，表示我们永远不可能完成这个课程
# 本题主要是通过dfs来判断是否有环，无环则可以完成这个课程
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list) # 先修课指向其他课
        for i in range(len(prerequisites)):
            cur, pre = prerequisites[i]
            graph[pre].append(cur) # pre->cur
        
        state = [0]*numCourses
        # 0: 未访问
        # 1: 正在访问
        # 2: 已经访问过
        def dfs(u):
            if state[u]==1: # 有其他的课程指向这个u，在当前i为节点的有向图内遇到了环
                return False # 遇到了环
            # 如果已经访问过了，则直接跳过
            if state[u]==2: # u和它所有的前置课的都已经检查完毕
                return True
            state[u]=1
            for v in graph[u]: # 遍历所有以v为先修课的课程
                if dfs(v)==False: # 以v为节点的有向图中有环，那么u中一定有环
                    return False
            state[u]=2 # 标记完成
            return True
            
        for i in range(numCourses): # iterate all courses
            if dfs(i)==False: # dfs(i)用于遍历所有需要课程i作为先修课的邻居课程
                return False
        return True

numCourses = 2
prerequisites = [[1,0]]
solution = Solution()
res = solution.canFinish(numCourses, prerequisites)
print(res)