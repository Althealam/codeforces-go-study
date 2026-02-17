class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0
        while i<len(bits)-1:
            if bits[i]==1:
                i+=2
            else:
                i+=1
            print("Current i:", i)
        return i==len(bits)-1

bits = [1, 1, 1, 0]
sol = Solution()
res = sol.isOneBitCharacter(bits)
print(res)