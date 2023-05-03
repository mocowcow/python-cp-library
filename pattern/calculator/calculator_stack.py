class Solution:
    def calculate(self, s: str) -> int:
        s+="+"
        st = []
        sign = "+"
        num = 0

        for c in s:
            if c == " ":
                pass
            if c.isdigit():
                num = num*10+int(c)
            elif c == "(":
                st.append(sign)
                sign = "+"
                st.append("(")
            elif c in "+-*/)":
                if sign == "+":
                    st.append(num)
                elif sign == "-":
                    st.append(-num)
                elif sign == "*":
                    st[-1] *= num
                elif sign == "/":
                    st[-1] = int(st[-1]/num)
                if c == ")":
                    num=0
                    while st[-1]!="(":
                        num+=st.pop()
                    st.pop()
                    sign=st.pop()
                else:
                    num = 0
                    sign = c

        return sum(st)
