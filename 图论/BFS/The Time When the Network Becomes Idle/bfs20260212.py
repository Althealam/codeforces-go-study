# The earlist second:
# 1. get the minimal distance from each node to 0 node
# 2. get the round distance like round=2*min_distance (cause the message will go with the same path twice)
# 3. the time that data server send the messages: 0, pi, 2pi, ..., npi
# we have to find the time that the dataserver send the message for the last time
# the last time the data server send the message satisfies: k*pi<round_distance[i]
# k*pi<=round_distance[i]-1==>k<=(round_distance[i]-1)/pi
# the maximum k shoule be (round_distance[i]-1)/pi, this is the last time the dataserver send the message 
# then we could get the last message time from all the data servers
# 4. find the end time for the last message


# analysis: get the earlist time ==> get the receive time of last message for every dataserver (receive time = send_time+round_time)
# ==> get the send time of last message for every dataserver ==> get the count of the last message of every dataserver + the round_time for every dataserver
# (1) round_time = 2*min_distance (min_distance can get by using bfs)
# (2) let k be the count of the last message: k*patience[i]<round_time[i], then k*patience[i]<=round_time[i]-1, k<=(round_time[i]-1)//patience[i]
# then, the send time of last email for every data server should be patience[i]*k
# Conclude: 
# (1) the send time of last email for every data server should be patience[i]*k
# (2) the receive time of last email for every data server should be round_time[i]+patience[i]*k
# the earlest time for the system should be max(round_time[i]+patience[i]*k)

from collections import defaultdict, deque
class Solution:
    def networkBecomesIdle(self, edges: list[list[int]], patience: list[int]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def bfs():
            dist = [-1]*len(patience) # dist[i] means the minimal distance from node 0 to node i
            dist[0] = 0 # initialziation
            q = deque()
            q.append(0)
            while q:
                cur_node = q.popleft()
                for neighbor_node in graph[cur_node]:
                    if dist[neighbor_node]==-1:
                        dist[neighbor_node]=dist[cur_node]+1
                        q.append(neighbor_node)
            return dist

        dist = bfs()
        round_dist = [x*2 for x in dist]

        # last_send_index means the last message is the i-th message
        last_send_index = [0]*len(patience)
        for i in range(1, len(dist)): # iterate all the node and get the last time the dataserver i send the message
            last_send_index[i] = (round_dist[i]-1)//patience[i]
        
        # last_send_min means the time for the last message 
        last_send_min = [0]*len(patience)
        for i in range(1, len(dist)):
            last_send_min[i] = last_send_index[i]*patience[i]

        # last finish time for each nodes
        last_finish_time = [0]*len(patience)
        for i in range(1, len(dist)):
            last_finish_time[i] = last_send_min[i]+round_dist[i]

        return max(last_finish_time)+1

edges = [[0,1],[1,2]]
patience = [0,2,1]
solution = Solution()
res = solution.networkBecomesIdle(edges, patience)
print(res)