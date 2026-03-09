# [3], [3, 1], [3, 1, 2], [3, 1, 2, 4]
# [1], [1, 2], [1, 2, 4]
# [2], [2, 4]
# [4]

# 判断每个元素作为最小值出现了几次
# 1: 6 ==> [3, 1], [3, 1, 2], [1], [1, 2], [1, 2, 4], [3, 1, 2, 4]
# 2: 2 ==> [2], [2, 4]
# 3: [3]

# suppose element k is the element index which want to find the count
# suppose the cloest right element index which is smaller than k is i => the array [k...i] is the valid array which have smallest element k
# suppose the cloest left element index which is smaller than k is j => the array [j...k] is the valid array which have smallest element k
# left: [j, j+1, ..., k-1] ==> k-1-j+1 = k-j
# right: [k+1, k+2, ...., i] ==> i-k-1+1 = i-k
# in that case, we could have (k-j)*(i-k) intervals which have element index k as the smallest element

# for each element, we have to find the previous smaller element and next smaller element

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        previous_smaller = [-1]*len(arr) # increasing stack
        next_smaller = [len(arr)]*len(arr) # decreasing stack

        # find the next smaller（递减栈）
        stack = []
        for i in range(len(arr)):
            # current stack[-1] find the next smaller element, which is arr[i]
            while len(stack)!=0 and arr[i]<arr[stack[-1]]:
                index = stack.pop()
                next_smaller[index] = i
            stack.append(i)
        
        # find the previous smaller（递增栈）
        stack = []
        for i in range(len(arr)):
            # if arr[stack[-1]]>=arr[i], it means that arr[stack[-1]] can not be the previous smaller element for every element after i
            while len(stack)!=0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            previous_smaller[i] = stack[-1] if stack else -1
            stack.append(i)
    
        MOD = 10**9+7
        count = 0
        for i in range(len(arr)):
            count+=arr[i]*(i-previous_smaller[i])*(next_smaller[i]-i)
        return count%MOD