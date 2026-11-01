# 遇到前面一位大于后面一位，就把前一位减去1，后面的都变成9
# 必须要从右往左操作
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        mark = len(digits)
        for i in range(len(digits)-1, 0, -1):
            if int(digits[i-1])>int(digits[i]): # 前面一位大于后面一位
                # 前面一位减去1
                digits[i-1] = str(int(digits[i-1])-1)
                # 执行了减去1操作后，该数字后面的数字都要变成9
                mark = i
        for i in range(mark, len(digits)):
            digits[i] = '9'
        return int(''.join(digits))