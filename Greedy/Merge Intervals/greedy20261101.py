class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals_new = sorted(intervals)
        ans = []
        if len(intervals_new)==0:
            return 0
        for start, end in intervals_new:
            if not ans or ans[-1][1]<start: # ans里面的区间和当前的区间有交集
                ans.append([start, end])
            else: 
                # 有交集，延长ans里面的区间
                ans[-1][1] = max(ans[-1][1], end)
        return ans
