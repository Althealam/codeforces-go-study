# [1, 2, 1, 9]
# [0, 2, 0, 0]
# []
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        count = 0 
        for c in num:
            while len(stack)!=0 and count<k and int(c)<int(stack[-1]):
                stack.pop()
                count+=1
            stack.append(c)
        
        while len(stack)!=0 and count<k:
            stack.pop()
            count+=1
        
        res = ''.join(stack)
        i = 0
        while i<len(res) and res[i]=='0':
            i+=1
        res = res[i:]
        return res if res else '0'

        