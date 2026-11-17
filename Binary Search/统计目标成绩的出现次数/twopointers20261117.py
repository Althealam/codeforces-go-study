class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        if len(scores)==0:
            return 0
        ind = self.binary_search(scores, target)
        if ind==-1:
            return 0
        cnt = 1
        left, right = ind, ind
        while left>0 and scores[left]==scores[left-1]:
            left-=1
            cnt+=1
        while right<len(scores)-1 and scores[right]==scores[right+1]:
            right+=1
            cnt+=1
        return cnt


    def binary_search(self, scores, target):
        left, right = 0, len(scores)-1
        while left<=right:
            mid = (left+right)//2
            if scores[mid]==target:
                return mid
            elif scores[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1