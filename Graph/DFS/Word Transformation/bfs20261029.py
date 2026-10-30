# 无权重的最短路径问题 -> bfs
from collections import deque

def isvalid(str1, str2):
    if len(str1)!=len(str2):
        return False
    diff = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]!=str2[j]:
                diff+=1
    return diff==1

def bfs(beginStr, endStr, strList):
    queue = deque([])
    queue.append((beginStr, 1))
    visited = [False]*len(strList)
    while queue:
        curStr, curStep = queue.popleft()
        if curStr == endStr:
            return curStep
        for i in range(len(strList)):
            if not visited[i] and is_valid(curStr, strList[i]):
                visited[i] = True
                queue.append((strList[i], curStep+1))

    return 0
 
def main():
    n = int(input())
    beginStr, endStr = input().split()
    strList = []
    for i in range(n):
        strList.append(int().strip())
    res = bfs(beginStr, endStr, strList)
    return res