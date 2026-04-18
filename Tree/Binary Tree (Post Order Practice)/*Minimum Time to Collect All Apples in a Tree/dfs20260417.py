# 1. 题目类型：自底向上
# 2. DFS三部曲：获取从node节点出发收集该子树上所有苹果的最小时间
#（1）携带参数：当前节点node
#（2）返回值含义：从node根节点出发收集该子树上所有苹果的最小时间
#（3）终止条件：遇到空节点则返回0
#（4）单层递归的逻辑
# - 调用DFS获取左右子树收集苹果所需要的最小时间leftime, rightime
# - 如果lefttime=righttime=0并且hasApple[nodeidx]=True: return 2
# - 如果lefttime!=0 and righttime!=0: return lefttime+righttime+2
# - 如果lefttime!=0 or righttime!=0: return max(lefttime, righttime)+2
# - 如果lefttime=righttime=0并且hasApple[nodeidx]=False: return 0

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for parent, child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        return self.dfs(0, hasApple, graph, -1)
        
    
    def dfs(self, nodeidx, hasApple, graph, parentidx):
        if nodeidx is None:
            return 0
        res = 0 # 收割当前子树的所有苹果的最小时间  
        for childidx in graph[nodeidx]:
            if childidx==parentidx:
                continue
            childtime = self.dfs(childidx, hasApple, graph, nodeidx)
            if childtime>0 or hasApple[childidx]: # 孩子子树上有苹果一定要收集
                res+=childtime+2
        return res
        