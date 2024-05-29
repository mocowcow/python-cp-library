

# 將不重複出現的小寫字母轉成bit mask
def lower_as_mask(s):
    n = 0
    for c in s:
        n |= 1 << (ord(c) - 97)
    return n

# s1 = 'abc'
# print(bin(lower_to_bit(s1)))
# s2 = 'asdzxc'
# print(bin(lower_to_bit(s2)))


# 字串s的冪集合及對應遮罩
def all_permutations(s):
    N = len(s)
    d = {}
    for mask in range(1 << N):
        sub = []
        for i in range(N):
            if mask & (1 << i):
                sub.append(s[i])
        d[mask] = sub
    return d

# s = '1357'
# permu = all_permutations(s)
# for k, v in permu.items():
#     print(bin(k), v)


# 將第 i 個位元設為 0
def clear_bit(mask, i):
    return mask & ~(1 << i)


# 將第 i 個位元設為 1
def set_bit(mask, i):
    return mask | (1 << i)


# 檢查是否為 2 的次方數
def is_pow_of_2(n):
    if n == 0:
        return False
    return n & (n-1) == 0


# 取得最低位的 1 位元
def low_bit(n):
    return n & -n  # n & (~n+1)
