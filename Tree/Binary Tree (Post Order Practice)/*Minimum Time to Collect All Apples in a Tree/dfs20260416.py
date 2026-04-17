# 1. 题目类型：自底向上
# 2. DFS三部曲：获取以node为根的子树，收集完所有苹果并返回到node所花费的时间
#（1）携带参数：当前节点node，父亲节点parent
#（2）返回值含义：以node为根节点的子树，收集完所有苹果返回到node所花费的时间
#（3）单层递归的逻辑
# - 遍历所有的child
# - 如果dfs(child)>0说明子树深度有苹果，当前节点到孩子的这条边必须走，因此+2
# - 如果dfs(child)=0，但是hasApple[child]=True，说明孩子本人为苹果，因此+2

# 注意：edges是无向边，并不是代表第一个元素一定是父亲节点，第二个元素一定是孩子节点
# 一定要在dfs里使用parentidx，避免无限循环，因此graph[parent]有children，graph[children]也有parent，因此遍历graph的时候会导致重复

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            parent, children = edge
            graph[parent].append(children)
            graph[children].append(parent)
        
        return self.dfs(0, -1, graph, hasApple)
        
        
    def dfs(self, nodeidx, parentidx, graph, hasApple):
        total_time = 0
        for child in graph[nodeidx]:
            if child==parentidx: # 防止回流
                continue
            child_time = self.dfs(child, nodeidx, graph, hasApple)
            if child_time>0 or hasApple[child]:
                total_time+=child_time+2
        return total_time