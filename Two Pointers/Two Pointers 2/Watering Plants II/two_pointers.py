class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        a, b = capacityA, capacityB
        i, j = 0, len(plants)-1
        while i<j:
            # Alice给植物i浇水
            if a<plants[i]: # 没有足够的水，重新灌满水壶
                ans+=1 # 灌满水壶次数加上1
                a = capacityA # 灌满水壶后的总容量
            # 减去当前植物需要的水量
            a-=plants[i]
            i+=1

            # Bob给植物j浇水
            if b<plants[j]:
                ans+=1
                b = capacityB
            b-=plants[j]
            j-=1
        
        # 如果Alice和Bob到达同一个植物
        if i==j and max(a, b)<plants[i]:
            # 没有足够的水，重新灌满水壶
            ans+=1
        return ans
        