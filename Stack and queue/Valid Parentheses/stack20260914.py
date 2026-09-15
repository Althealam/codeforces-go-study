class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i]=='(':
                st.append(")")
            elif s[i]=='[':
                st.append("]")
            elif s[i]=="{":
                st.append("}")
            else:
                if len(st)==0:
                    return False
                else:
                    node = st.pop()
                    if node==s[i]:
                        continue
                    else:
                        return False
        return True if len(st)==0 else False