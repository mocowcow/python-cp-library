import random

MOD1 = 1_000_000_901
MOD2 = 1_000_015_279
MOD3 = 1_000_000_000_000_000_000_003


class RollingHash:
    def __init__(self, s, mod):
        # self.s = s
        self.mod = mod
        # base = random.randint(2, mod-1)
        base = 87
        ps = self.ps = [0] * (len(s) + 1)
        base_pow = self.base_pow = [1] * (len(s) + 1)
        for i, c in enumerate(s):
            ps[i+1] = (ps[i] * base + ord(c)) % mod
            base_pow[i+1] = (base_pow[i] * base) % mod

    def get(self, L, R):
        # print(self.s[L:R+1])
        return (self.ps[R+1] - self.ps[L] * self.base_pow[R-L+1]) % self.mod


class DoubleHash:
    def __init__(self, s, mod1, mod2):
        self.h1 = RollingHash(s, mod1)
        self.h2 = RollingHash(s, mod2)

    def get(self, L, R):
        return (self.h1.get(L, R), self.h2.get(L, R))


s = "levellevelasdasdaaasdaaaaaaaaaaa"

dh = DoubleHash(s, MOD1, MOD2)


def test_same(s):
    N = len(s)
    dh = DoubleHash(s, MOD1, MOD2)
    for _ in range(1000):
        size = random.randint(1, N)
        i1 = random.randint(0, N - size)
        i2 = random.randint(0, N - size)

        hash_eq = dh.get(i1, i1 + size - 1) == dh.get(i2, i2 + size - 1)
        s_eq = s[i1:i1+size] == s[i2:i2+size]

        assert (hash_eq == s_eq)
    print('passed')


test_same(s)
