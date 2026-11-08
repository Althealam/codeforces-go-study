class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                num1 = st.pop()
                num2 = st.pop()
                if token=="+":
                    st.append(int(num1)+int(num2))
                elif token=='-':
                    st.append(int(num2)-int(num1))
                elif token=='*':
                    st.append(int(num1)*int(num2))
                else:
                    quotinet = abs(int(num2))//abs(int(num1))
                    if (int(num2)<0)!=(int(num1)<0):
                        quotinet = -quotinet
                    st.append(quotinet)
            else:
                st.append(token)
        return int(st.pop())