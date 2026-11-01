class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        queue = collections.deque()
        indegree = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a) # 先修课->当前课
            indegree[a]+=1 # 当前课的入度
        
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i) # 当前课程没有先修课要求，可以先入队列 -> 如果所有的课都有先修课要求，则说明有环，无法开始
        
        path = []
        while queue: # 只有入度为0的课程可以放到queue中
            node = queue.popleft()
            path.append(node)
            for nxt in graph[node]: # 遍历以这门课为先修课的所有课程
                indegree[nxt]-=1 # nxt的入度减去1，表示已经修了一门先修课
                if indegree[nxt]==0: # 这门课的所有先修课都已经修完了
                    queue.append(nxt)
        
        return True if len(path)==numCourses else False