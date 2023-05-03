
def calculate(s: str) -> int:
    s += "#"  # 哨兵，方便求最後一個num
    i = 0

    def f():
        nonlocal i
        st = []
        sign = "+"
        num = 0

        while i < len(s):
            c = s[i]

            if c == " ":  # 無視空格
                i += 1
                continue
            if c.isdigit():
                num = num*10+int(c)
            elif c == "(":  # 遞迴求括號內的值
                i += 1
                num = f()
            elif c in "+-*/)" or i == len(s)-1:  # 哨兵"#"或是右括號")"時，要將當前的num值加入答案
                if sign == "+":
                    st.append(num)
                elif sign == "-":
                    st.append(-num)
                elif sign == "*":
                    st[-1] *= num
                elif sign == "/":
                    st[-1] = int(st[-1]/num)
                if c == ")":  # 括號內計算完畢，退出遞迴
                    break
                num = 0
                sign = c
            # 下一個字元
            i += 1

        return sum(st)

    return f()
