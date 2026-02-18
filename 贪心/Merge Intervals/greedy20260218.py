class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals)==0:
            return res
        intervals.sort(key=lambda x: x[0])
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1]>=intervals[i][0]: # the interval in the result array overlap with the interval i 
                intervals[i][0] = min(res[-1][0], intervals[i][0])
                intervals[i][1] = max(res[-1][1], intervals[i][1])
                res.pop()
            res.append(intervals[i])
        return res