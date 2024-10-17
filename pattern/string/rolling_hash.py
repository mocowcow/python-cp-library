import random

# LC28 https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# LC187 https://leetcode.com/problems/repeated-dna-sequences/
# LC1044 https://leetcode.com/problems/longest-duplicate-substring/
# LC1392 https://leetcode.com/problems/longest-happy-prefix/
# LC3213 https://leetcode.com/problems/construct-string-with-minimum-cost/
# LC3292 https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/
# LC3303 https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/


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
        # self.s = s
        self.mod1 = mod1
        self.mod2 = mod2
        # base = random.randint(2, mod-1)
        base1 = 87
        base2 = 116
        ps1 = self.ps1 = [0] * (len(s) + 1)
        ps2 = self.ps2 = [0] * (len(s) + 1)
        base_pow1 = self.base_pow1 = [1] * (len(s) + 1)
        base_pow2 = self.base_pow2 = [1] * (len(s) + 1)
        for i, c in enumerate(s):
            ps1[i+1] = (ps1[i] * base1 + ord(c)) % mod1
            ps2[i+1] = (ps2[i] * base2 + ord(c)) % mod2
            base_pow1[i+1] = (base_pow1[i] * base1) % mod1
            base_pow2[i+1] = (base_pow2[i] * base2) % mod2

    def get(self, L, R):
        # print(self.s[L:R+1])
        h1 = (self.ps1[R+1] - self.ps1[L] * self.base_pow1[R-L+1]) % self.mod1
        h2 = (self.ps2[R+1] - self.ps2[L] * self.base_pow2[R-L+1]) % self.mod2
        return (h1, h2)


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
