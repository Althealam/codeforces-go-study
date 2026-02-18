# intervals[i-1], intervals[i]
# intervals[i-1][1]>=intervals[i][0]

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        ans = 1
        for i in range(1, len(points)):
            if points[i-1][1]>=points[i][0]:
                points[i][0] = max(points[i-1][0], points[i][0])
                points[i][1] = min(points[i-1][1], points[i][1])
            else:
                ans+=1
        return ans