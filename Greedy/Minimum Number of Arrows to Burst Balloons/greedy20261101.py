class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points_new = sorted(points)
        ans = 1
        for i in range(1, len(points_new)):
            if points_new[i-1][1]>=points_new[i][0]:
                points_new[i][0] = max(points_new[i-1][0], points_new[i][0])
                points_new[i][1] = min(points_new[i-1][1], points_new[i][1])
                # 可以用同一个箭
            else:
                # 不能用同一个箭
                ans+=1
        return ans
            