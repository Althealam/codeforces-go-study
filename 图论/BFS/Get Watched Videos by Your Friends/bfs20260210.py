# 从id开始BFS，找到距离=level的所有人，获取他们的视频，统计这些视频的出现频率，排序输出这些视频
from typing import Any


from collections import Counter, deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        cnt = Counter()
        def bfs(i, level):
            dist = [False]*len(friends) # 判断这个朋友是否遇到过
            queue = deque[Any]()
            queue.append((i, 0)) # 目前遍历的节点是i，并且在第0层
            ans = [] # 存储level为level的所有朋友
            while queue:
                u, cur_level = queue.popleft()
                dist[u] = True
                if cur_level==level:
                    ans.append(u)
                    continue # 截断，此时不需要再继续扩展u的邻居
                for v in friends[u]: # 遍历u的所有朋友
                    if dist[v]==False: # 当前没有没有遇到过
                        dist[v] = True
                        queue.append((v, cur_level+1)) 
            return ans   

        id_friends = bfs(id, level)  # 获取编号为id的level为level的所有朋友
        for friend in id_friends: # 遍历其level为level的所有朋友
            for video in watchedVideos[friend]: # 获取这些朋友看的视频
                cnt[video]+=1
        # print(cnt)
        return sorted(cnt.keys(), key=lambda x: (cnt[x], x))

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 2
solution = Solution()
res = solution.watchedVideosByFriends(watchedVideos, friends, id, level)
print(res)