
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 傳入dy,dx
# 回傳dy/dx最簡分數
def fraction_slope(a, b):
    _gcd = gcd(a, b)
    return (a//_gcd, b//_gcd)


# 判斷三點共線
# (b[1]-a[1]) / (b[0]-a[0]) == (c[1]-b[1]) / (c[0]-b[0])
def same_line(a, b, c):
    return (b[1]-a[1])*(c[0]-b[0]) == (c[1]-b[1])*(b[0]-a[0])

