# sum_%p==0 ==> (sum(nums)-[i..j]_%p==0 ==> sum(nums)%p==[i..j]%p ==> sum(nums)%p==(prej-prei)%p
# ==> sum(nums)%p==(prej%p)-(prei%p) ==> need = prej%p-prei%p
# ==> prei%p = prej%p-need （需要反解出符合条件的i），并且存储这个i的出现位置

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sum_ = sum(nums)
        need = sum_%p
        if need==0:
            return 0
        pre = 0
        ans = len(nums)
        cnt = defaultdict(int)
        cnt[0] = -1
        for i in range(len(nums)):
            pre+=nums[i]
            cur = pre%p
            target = (cur-need)%p
            if target in cnt:
                ans = min(ans, i-cnt[target])
            cnt[cur] = i # 存储最新的位置
        return ans if ans<len(nums) else -1
       
            

        