
def calculate(s: str) -> int:
    i = 0
    s += ")"

    def f():
        nonlocal i
        st = []
        sign = "+"
        num = 0

        while i < len(s):
            c = s[i]

            if c == " ":
                pass
            if c.isdigit():
                num = num*10+int(c)
            elif c == "(":
                i += 1
                num = f()
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
                    break
                num = 0
                sign = c
            ##
            i += 1
        return sum(st)

    return f()
