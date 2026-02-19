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
        
        prefix_sum = [0]*len(hours)
        for i in range(len(prefix_sum)):
            if i==0:
                prefix_sum[i] = hours[i]
            else:
                prefix_sum[i] = prefix_sum[i-1]+hours[i]
        
        ans = 0
        cnt = {}
        cnt[0] = -1
        for i in range(len(hours)):
            current_prefix = prefix_sum[i]
            if current_prefix>0: # current interval [0..i] is great interval
                ans = max(ans, i+1)
            target_prefix = current_prefix-1
            if target_prefix in cnt:
                ans = max(ans, i-cnt[target_prefix])
            if current_prefix not in cnt:
                cnt[current_prefix] = i
        return ans


        