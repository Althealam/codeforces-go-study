class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals_new = sorted(intervals)
        ans = 0
        for i in range(1, len(intervals_new)):
            if intervals_new[i-1][1]>intervals_new[i][0]:
                # 有重叠的，要挪走一个区间
                ans+=1
                # 移走一个区间，并保留结束更早的那个
                # intervals_new[i][0] = max(intervals_new[i-1][0], intervals_new[i][0])
                intervals_new[i][1] = min(intervals_new[i-1][1], intervals_new[i][1])      
        return ans