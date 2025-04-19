
# converse x to b-base
def convertToBase(x: int, b: int):
    if x == 0:
        return "0"
    sign = "" if x >= 0 else "-"
    x = abs(x)
    res = []
    while x > 0:
        r = x % b
        res.append(str(r))
        x //= b
    res.reverse()
    return sign + "".join(res)
