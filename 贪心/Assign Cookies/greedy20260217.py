class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0 # means the number of content children
        for i in range(len(s)): # iterate all cookie
        # if the cookie i can not feed the children res, then it could also not feed the children res+1
            if res<len(g) and s[i]>=g[res]:
                res+=1
        return res