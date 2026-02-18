# {12: [0, 9]}
# objective: find the frequence of value in the [left, right]
# find the first direction which is larger than the left index in the subarray, the first direction which is smaller than the right index in the subarray
# Example: [0, 9] is the subarray, [2, 3] is the left and right
# return 0 cause left_new and right_new is None
# return length of the subarray right_new-left_new+1
from bisect import bisect_left
from collections import defaultdict
class RangeFreqQuery:
    def __init__(self, arr: list[int]):
        self.pos = defaultdict(list)

        for index, num in enumerate(arr):
            self.pos[num].append(index)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos:
            return 0
        arr = self.pos[value]
        l = self.bisect_left(arr, left)
        r = self.bisect_right(arr, right)
        return r-l
    # def query(self, left: int, right: int, value: int) -> int:
        # given subarray [1, 7] and left=0, right = 11
        # find the first index which is larger than the left
        # subarray = self.pos[value]
        # print("subarray:", subarray)
        # print("left:", left)
        # print("right:", right)
        # left_new_index, right_new_index = None, None
        # for i in range(len(subarray)):
        #     if subarray[i]>=left:
        #         left_new_index = i
        #         break
        # for i in range(len(subarray)-1, -1, -1):
        #     if subarray[i]<=right:
        #         right_new_index = i
        #         break
        # print("left_new_index:", left_new_index)
        # print("right_new_index:",right_new_index)
        # return right_new_index-left_new_index+1 if left_new_index!=None and right_new_index!=None else 0

    def bisect_left(self, arr, target):
        # find the first direction which is larger than target
        # arr: [1, 3, 5] target = 4 return: 5
        l, r = 0, len(arr)
        while l<r:
            mid = (l+r)//2
            if arr[mid]<target:
                l=mid+1
            else:
                r=mid
        return l


    def bisect_right(self, arr, target):
        # find the first direction which is larger than right
        # arr: [1, 3, 5] target = 4 return: 5
        l, r = 0, len(arr)
        while l<r:
            mid = (l+r)//2
            if arr[mid]<=target:
                l = mid+1
            else:
                r = mid
        return l



# Your RangeFreqQuery object will be instantiated and called as such:
arr = [1,1,1,2,2]
obj = RangeFreqQuery(arr)
left, right, value = [0, 1, 2]
param_1 = obj.query(left,right,value)
print(param_1)