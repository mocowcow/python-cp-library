
import random
import string

# KMP 求子字串起點
# LC2851 https://leetcode.com/problems/string-transformation/
# LC3008 https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/


# LPS (Longest Prefix Suffix)
# LC1392 https://leetcode.com/problems/longest-happy-prefix/


# PMT for KMP string search
def partial_match_table(s):
    N = len(s)
    pmt = [0]*N
    i, j = 1, 0
    while i < N and j < N:
        if s[i] == s[j]:
            j += 1
            i += 1
            pmt[i - 1] = j
        elif j == 0:
            i += 1
        else:
            j = pmt[j - 1]
    return pmt


# PMT optimized version
def prefix_function(s):
    N = len(s)
    pmt = [0]*N
    for i in range(1, N):
        j = pmt[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pmt[j - 1]
        if s[i] == s[j]:
            j += 1
        pmt[i] = j
    return pmt


# search p in s, return first index.
# return -1 if not found
def KMP(s, p):
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            return i - j + 1
    return -1


# search p in s, return every starting idnex of p
def KMP_all(s, p):
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    res = []
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            res.append(i - j + 1)
            j = pmt[j - 1]
    return res


def test_same(g, f):
    for _ in range(1000):
        s = "".join(random.choice(string.ascii_letters) for _ in range(1000))
        assert (g(s) == f(s))
    print('passed')


test_same(partial_match_table, prefix_function)
