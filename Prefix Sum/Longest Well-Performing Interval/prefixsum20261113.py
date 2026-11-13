# goal: find the maximal length of the interval with the sum larger than 0
# pre[j]-pre[i]>0 => pre[i]<=pre[j]-1 对于每个j，寻找一个更早的位置i，满足pre[i]<pre[j]，即target=pre[j]-1
class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        for i in range(len(hours)):
            if hours[i]>8:
                hours[i] = 1
            else:
                hours[i] = -1
        
        pre = [0]*len(hours)
        for i in range(len(hours)):
            if i==0:
                pre[0] = hours[0]
            else:
                pre[i] = pre[i-1]+hours[i]
        max_len = 0
        hash = {}
        hash[0] = -1
        for i in range(len(pre)):
            if pre[i]>0:
                max_len = i+1
            else:
                target = pre[i]-1
                if target in hash:
                    max_len = max(max_len, i-hash[target])
            if pre[i] not in hash:
                hash[pre[i]] = i
        return max_len
