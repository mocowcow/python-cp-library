
# PMT for KMP string search
def partial_match_table(s):
    N = len(s)
    pmt = [0]*N
    i, j = 1, 0
    while i < N and j < N:
        if s[i] == s[j]:
            j += 1
            i += 1
            pmt[i-1] = j
        elif j == 0:
            i += 1
        else:
            j = pmt[j-1]
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
            j = pmt[j-1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            return i-j+1
    return -1


# search p in s, return every starting idnex of p
def KMP_freq(s, p):
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    res = []
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j-1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            res.append(i-j+1)
            j = pmt[j-1]
    return res


test_cases = []
test_cases.append("abac")
test_cases.append("abababca")
test_cases.append("12312313123123112312")

for tc in test_cases:
    assert partial_match_table(tc) == prefix_function(tc)
