class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_, sum_ = 1, 0
        while n!=0:
            x, n = n%10, n//10
            product_*=x
            sum_+=x
        return product_-sum_

# time: O(logn)
# space: O(1)