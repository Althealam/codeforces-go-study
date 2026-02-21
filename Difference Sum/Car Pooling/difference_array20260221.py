# [0 0 0 0 0 0 0 0]
# [0 2 2 2 2 2 0 0] ==> [0 2 0 0 0 0 0 0]
# [0 2 2 5 5 5 5 5] ==> [0 2 0 3 0 0 0 0 ]
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0]*1001
        for num, from_, to in trips:
            diff[from_]+=num
            diff[to]-=num # 注意这里不是diff[to+1]-=num，因为只要到站点，他们就会下车
         
        array = [0]*1001
        array[0] = diff[0]
        for i in range(1000):
            if i!=0:
                array[i] = array[i-1]+diff[i]
            if array[i]>capacity: # 注意：一定要记得对0进行判断
                return False
        return True



sol = Solution()
trips = [[9,0,1], [3,3,7]]
capacity = 4
res = sol.carPooling(trips, capacity)
print(res)