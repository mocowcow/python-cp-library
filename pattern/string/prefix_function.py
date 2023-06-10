
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
    pi = [0]*N
    for i in range(1, N):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


test_cases = []
test_cases.append("abac")
test_cases.append("abababca")
test_cases.append("12312313123123112312")

for tc in test_cases:
    assert partial_match_table(tc) == prefix_function(tc)
