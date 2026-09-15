class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if len(st)==0:
                st.append(s[i])
            else:
                if s[i]==st[-1]:
                    st.pop()
                else:
                    st.append(s[i])
        return "".join(st[:])