# [[1, 2], [1, 3], [2, 3], [3, 4]]
# intervals[i-1][1]>=intervals[i][0] 2>=1 ==> the two intervals overlap [1, 2] and [1, 3] ==> res+=1
# A[1]<B[1]: we have to keep the A internal (the optimal interval)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i-1][1]>intervals[i][0]: # overlap happends
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
                intervals[i][0] = max(intervals[i-1][0], intervals[i][0])
                res+=1
        return res

