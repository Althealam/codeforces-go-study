# 核心思想：遇到[时保存当前状态，遇到]时解码当前括号中的字符串，再和之前的字符串拼接
# 重要特征：括号可以嵌套，并且必须先处理最里面的括号 -> 后进入的括号，要先进行解码，因此是last in first out
# 栈内存储的东西：num表示当前括号需要重复多少次，res表示进入括号之前已经构建好的字符串
# 1. 遇到数字：更新重复次数num
# 2. [：将(num, res)入栈，重置当前状态
# 3. ]：弹出之前的状态，完成解码和拼接
# 4. 普通字母，追加到res
# 时间复杂度：假设n是输入的字符串长度，L时最终解码的字符串长度，时间复杂度为O(n+L^2)
# 空间复杂度：O(n+L)



class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        k = 0
        for st in s:
            if "0"<=st<="9": # 数字有可能是12/13这种大于10的数字
                k = k*10+int(st)
            elif st=='[':
                stack.append((res, k))
                res, k = "", 0 # 接下来要单独处理当前括号内部的字符串
            elif st==']': # 新字符串=之前的字符串+重复次数*当前字符串
                last_res, last_k = stack.pop()
                res = last_res+res*last_k
            else: # 遇到普通的字符
                res+=st
        return res