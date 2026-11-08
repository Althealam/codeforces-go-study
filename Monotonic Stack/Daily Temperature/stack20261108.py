class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        st = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[i]>st[-1][0]:
                temp, index = st.pop()
                ans[index] = i-index
            st.append([temperatures[i], i])
        return ans


