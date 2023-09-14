

def next_table(p):
    N = len(p)
    table = [0]*(N+1)  # table[N] is needed for multiple matches
    table[0] = -1
    i, j = 1, 0
    while i < N:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            table[i] = j
        else:
            j = table[j]
    return table


def KMP(s, p):  # search p in s
    M, N = len(s), len(p)
    i = j = 0
    table = next_table(p)
    while i < M:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = table[j]
        if j == N:  # change here if you want multiple matches
            return i-j
    return -1


print(KMP('abaababaca', 'abac'))
