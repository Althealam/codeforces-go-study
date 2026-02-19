# the number of tiring days (hour>8) is stricly larger than the number of non-tiring days (hour<=8)
# >8 transform to 1, <=8 transform to -1 
# great interval: sum(1)>sum(-1) ==> prefix_j-prefix_i>0
# prefix_j-prefix_i>0 ==> prefix_j<prefix_i and max(j-i) ==> prefix_i = prefix_j-1
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        for i in range(len(hours)):
            if hours[i]>8:
                hours[i] = 1
            else:
                hours[i] = -1
                
        ans = 0
        cnt = {}
        cnt[0] = -1
        pre = 0
        for i in range(len(hours)):
            pre+=hours[i]
            if pre>0:
                ans = max(ans, i+1) # [0..2] is great internel, then its length is i+1
            target = pre-1
            if target in cnt:
                ans = max(ans, i-cnt[target])
            if pre not in cnt:
                cnt[pre] = i
        return ans
