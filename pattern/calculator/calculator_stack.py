
def calculate(s: str) -> int:
    s += "#"  # 哨兵，方便求最後一個num
    i = 0
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
        elif c == "(":  # 求num=括號內的值
            st.append(sign)  # 先把這個括號的運算子sign暫存到堆疊
            sign = "+"
            st.append("(")  # 然後左括號加入堆疊，用於之後配對
        elif c in "+-*/)" or i == len(s)-1:  # 哨兵"#"或是右括號")"時，要將當前的num值加入答案
            if sign == "+":
                st.append(num)
            elif sign == "-":
                st.append(-num)
            elif sign == "*":
                st[-1] *= num
            elif sign == "/":
                st[-1] = int(st[-1]/num)
            if c == ")":  # 括號結束，求括號內的值
                num = 0
                while st[-1] != "(":  # 把括號內的值都加總
                    num += st.pop()
                st.pop()  # 丟掉配對完的左括號
                sign = st.pop()  # 把括號值所屬的運算子sign拿回來
            else:
                num = 0
                sign = c
        # 下一個字元
        i += 1

    return sum(st)
