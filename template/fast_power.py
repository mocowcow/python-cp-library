
def fastPower(base: int, p: int, mod: int)->int:
    res = 1
    while p:
        if p & 1:
            res = (res*base) % mod
        p >>= 1
        base = (base*base) % mod
    return res


print(fastPower(2, 10, 100))  # 1027 MOD 100 = 24
print(fastPower(3, 10, 100))  # 59049 MOD 100 = 49
