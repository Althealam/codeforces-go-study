class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in range(len(tokens)):
            if tokens[i] not in ("+", "-", "*", "/"):
                st.append(int(tokens[i]))
            else:
                n1 = st.pop()
                n2 = st.pop()
                if tokens[i]=='+':
                    tmp = n1+n2
                elif tokens[i]=='-':
                    tmp = n2-n1
                elif tokens[i]=='*':
                    tmp = n1*n2
                else:
                    if n1==0:
                        return None
                    else:
                        tmp = n2//n1 if n2//n1>0 else -(abs(n2)//abs(n1))
                st.append(tmp)
        return st.pop() 
