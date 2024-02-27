import random

MOD1 = 1000000901
MOD2 = 1000015279


class RollingHash:
    def __init__(self, s, mod):
        self.mod = mod
        base = random.randint(2, mod-1)
        ps = self.ps = [0]
        p = self.p = [1]
        for c in s:
            ps.append((ps[-1] * base + ord(c)) % mod)
            p.append(p[-1] * base % mod)

    def get(self, L, R):
        return (self.ps[R+1] - self.ps[L] * self.p[R-L+1]) % self.mod


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
