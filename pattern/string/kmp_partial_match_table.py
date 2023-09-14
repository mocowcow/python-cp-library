
def partial_match_table(s):  # PMT for KMP string search
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


def prefix_function(s):  # optimized version
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


def KMP(s, p):  # search p in s, return first index or -1
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j-1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            return i-j
    return -1


def KMP_freq(s, p):  # search p in s, return frequency of p
    M, N = len(s), len(p)
    pmt = prefix_function(p)
    j = 0
    cnt = 0
    for i in range(M):
        while j > 0 and s[i] != p[j]:
            j = pmt[j-1]
        if s[i] == p[j]:
            j += 1
        if j == N:
            cnt += 1
            j = pmt[j-1]
    return cnt


test_cases = []
test_cases.append("abac")
test_cases.append("abababca")
test_cases.append("12312313123123112312")

for tc in test_cases:
    assert partial_match_table(tc) == prefix_function(tc)
