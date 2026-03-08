# num=73, stack=[(73, 0)], res=[0, 0, 0, 0, 0, 0, 0, 0]
# num=74, stack=[(74, 1)], res=[1, 0, 0, 0, 0, 0, 0, 0]
# num=75, stack=[(75, 2)], res=[1, 1, 0, 0, 0, 0, 0, 0]
# num=71, stack=[(75, 2), (71, 3)], res = [1, 1, 0, 0, 0, 0, 0, 0]
# num=69, stack=[(75, 2), (71, 3), (69, 4)], res=[1, 1, 0, 0, 0, 0, 0, 0]
# num=72, stack=[(75, 2), (71, 3)], res=[1, 1, 0, 0, 5-4, 0, 0, 0]
#         stack=[(75, 2)], res = [1, 1, 0, 5-3, 5-4, 0, 0, 0]
#         stack=[(75, 2), (72, 5)]


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(stack)!=0 and temperatures[i]>stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = i-prev_index
            stack.append((temperatures[i], i))
        return res