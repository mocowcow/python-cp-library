
# 1連加到n
def sum1toN(n):
    return n*(n+1)//2


# m連加到n
# 梯形公式(上底+下底)*高/2
def sumMtoN(m, n):
    return (n+m)*(n-m+1)//2


# m連加到n
# 沒效率版
def mn(m, n):
    return n*(n+1)//2-(m-1)*(m)//2


# 最大公因數
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# 最大公因數
# 迴圈版
def gcd_iter(a, b):
    while a > 0:
        a, b = b % a, a
    return b


# 最小公倍數
def lcm(a, b):
    return a*b//gcd(a, b)


# 多個數最小公因數
def gcd_multi(nums):
    _gcd = 0
    for x in nums:
        _gcd = gcd(_gcd, x)
    return _gcd


# 多個數最小公倍數
def lcm_multi(nums):
    _lcm = 1
    for x in nums:
        _lcm = _lcm*x//gcd(_lcm, x)
    return _lcm
