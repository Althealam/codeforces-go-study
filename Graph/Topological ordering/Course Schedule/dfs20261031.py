class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b) # 表示学a之前要先学b

        state = [0]*numCourses # 用来标记状态

        def dfs(node):
            if state[node]==1: # 表示重复遇到
                return False
            if state[node]==2: 
                return True
            state[node] = 1 
            for pre in graph[node]:
                if not dfs(pre): # 表示pre已经在这条路径上遇到过了
                    return False 
            state[node] = 2
            return True

        for node in range(numCourses): # 遍历所有的课程
            if not dfs(node): # 判断当前节点是否有环，如果为false则表示有环
                return False
        return True