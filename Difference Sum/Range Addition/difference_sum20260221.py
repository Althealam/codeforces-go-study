# [0 0 0 0 0]
# [0 2 2 2 0]==>[0 2 0 0 -2]
# [0 2 5 5 3]==>[0 2 3 0 -2]
# [-2 0 3 5 3]==>[-2 2 3 2 -2]
# d[i]=a[i]-a[i-1]
# a[i]=d[0]+...+d[i]
# d[1]=a[1]-a[0]
# d[0]=a[0]
# a[1]=d[0]+d[1]
class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:
        difference = [0]*length
        for update in updates:
            left, right = update[0], update[1]
            increment = update[2]
            difference[left]+=increment
            if right<length-1:
                difference[right+1]-=increment
        
        array = [0]*length
        array[0] = difference[0]
        for i in range(1, length):
            array[i] = array[i-1]+difference[i]
        return array

length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
sol = Solution()
res = sol.getModifiedArray(length, updates)
print(res)