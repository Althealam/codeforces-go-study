# 整体思路：维护一个单调递减栈，当遇到更高的柱子时，计算能够形成凹槽的面积
# 计算凹槽面积的思路：找到左边界、右边界、凹槽底部，然后按照水平方向一层层计算雨水面积
# 1. 计算水的高度 h =min(height[right_index], height[left_index])-height[bottom_index]
# 2. 计算水的宽度 w = right_index-left_index-1
# 3. 计算雨水的面积：area = h*w 
# corner case
# 1. 少于三根柱子，输出为0
# 2. 相同高度，输出为0
class Solution:
    def trap(self, height: list[int]) -> int:
        st = []
        ans = 0
        for i in range(len(height)):
            while st and height[i]>height[st[-1]]:
                right_index = i
                bottom_index = st.pop()
                if st:
                    left_index = st[-1]
                    h = min(height[right_index], height[left_index])-height[bottom_index]
                    l = right_index-left_index-1
                    ans+=h*l
            st.append(i)
        return ans

