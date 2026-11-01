class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals_new = sorted(intervals)
        ans = []
        for i in range(1, len(intervals_new)):
            if intervals_new[i-1][1]>=intervals_new[i][0]:
                intervals_new[i][0] = min(intervals_new[i][0], intervals_new[i-1][0])
                intervals_new[i][1] = max(intervals_new[i][1], intervals_new[i-1][1])
                ans.append([intervals_new[i][0], intervals_new[i][1]])
            else:
                ans.append(intervals_new[i])
        return ans
