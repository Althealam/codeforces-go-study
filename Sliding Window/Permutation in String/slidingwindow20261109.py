from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        counter_s2 = Counter()
        for right, st in enumerate(s2):
            counter_s2[st]+=1
            left = right-len(s1)+1
            if left<0:
                continue
            if counter_s2==counter_s1:
                return True
            counter_s2[s2[left]]-=1
        return False