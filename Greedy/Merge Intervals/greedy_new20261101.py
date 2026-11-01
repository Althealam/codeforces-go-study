class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals_new = sorted(intervals)
        ans = []
        if len(intervals_new)==0:
            return 0
        ans.append(intervals_new[0])
        for i in range(1, len(intervals_new)):
            if intervals_new[i][0]<=ans[-1][1]:
                intervals_new[i][0] = min(intervals_new[i][0], ans[-1][0])
                intervals_new[i][1] = max(intervals_new[i][1], ans[-1][1])
                ans.pop()
            ans.append(intervals_new[i])
        return ans

