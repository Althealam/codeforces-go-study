# 1. define monotonic stack, and this stack will store the elements which do not meet the higher element (the element for right val) ==> this stack is non-increasing(only when the element is not higher than the value of the head of the stack, this element will be push into this stack, otherwise we will push the head of the stack)
# 2. iterate all number in height
# (1) if we find a element which have a higher value than the element in the head of the stack
# which means that the head of the stack already finds a bucket for it, then we can calculate its area, and the right val is this element, the bottom is the head of the stack, the left val is the other head of the stack(after we pop the head of the stack)
# (1.1) add the area to the ans
class Solution:
    def trap(self, height: List[int]) -> int:
        st = [] # store the index for the height, not the value
        ans = 0
        for i in range(len(height)):
            while len(st)!=0 and height[i]>height[st[-1]]: 
                right_index = i
                bottom_index = st.pop()
                if len(st)!=0:
                    left_index = st[-1]
                    h = min(height[right_index], height[left_index])-height[bottom_index]
                    l = right_index-left_index-1
                    ans+=h*l
            st.append(i)
        return ans

        