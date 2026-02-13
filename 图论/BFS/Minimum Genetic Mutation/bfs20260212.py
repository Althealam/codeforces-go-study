# 建图，让startGene, endGene和bank里面的字符串建立图，如果两个字符串之间只有一个字母不同，那么这两个字符串就有路径
# 每个合法gene=一个节点，每次改一个字符为一个路径，找到从startGene到endGene的最短路径

from collections import defaultdict, deque
from tracemalloc import start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        def bfs():
            queue = deque()
            queue.append((startGene, 0))

            visited = set()
            visited.add(startGene)

            genes = ['A', 'C', 'G', 'T']

            while queue:
                current, steps = queue.popleft()
                if current==endGene:
                    return steps
                
                for i in range(len(current)): # 遍历current gene的字符current[i]
                    for g in genes: # 尝试修改字符current[i]为g，判断一下修改后的字符串是否在bank中，如果在的话就有一个节点
                        if g!=current[i]:
                            new_gene = current[:i]+g+current[i+1:]

                            if new_gene in bank_set and new_gene not in visited:
                                visited.add(new_gene)
                                queue.append((new_gene, steps+1))
            return -1
                
        return bfs()

startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank = ["AACCGGTA"]
sol = Solution()
res = sol.minMutation(startGene, endGene, bank)
print(res)

