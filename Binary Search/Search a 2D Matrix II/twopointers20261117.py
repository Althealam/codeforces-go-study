# 每一行从左到右递增，每一列从上到下递增
# 左边的元素都比他小或者相等
# 下面的元素都比他大或者相等

# 时间复杂度：O(m+n)
# 空间复杂度：O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1 # 从右上角开始搜索
        while i>=0 and i<m and j>=0 and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]<target: # 这一行的元素都比target小
                i+=1
            elif matrix[i][j]>target: # 这一列的元素都比target大
                j-=1
        return False