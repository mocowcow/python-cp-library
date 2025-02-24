

# precompute all factorial and modular multiplicative inverse for factorial
# O(MX log EXP) where EXP = MOD-2
MOD = 10 ** 9 + 7
MX = 10 ** 5
f = [0] * (MX + 1)
f_inv = [0]*(MX + 1)
f[0] = f_inv[0] = 1
f[1] = f_inv[1] = 1
for i in range(2, MX + 1):
    f[i] = (f[i-1] * i) % MOD
    f_inv[i] = pow(f[i], -1, MOD)


# linear version
# O(MX)
MOD = 10 ** 9 + 7
MX = 10 ** 5
f = [0] * (MX + 1)
inv = [0] * (MX + 1)
f_inv = [0] * (MX + 1)
f[0] = inv[0] = f_inv[0] = 1
f[1] = inv[1] = f_inv[1] = 1
for i in range(2, MX + 1):
    f[i] = (f[i-1] * i) % MOD
    inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
    f_inv[i] = f_inv[i-1] * inv[i] % MOD


# combanations of n choose k
def comb(n, k):
    if n < k:
        return 0
    res = f[n] * f_inv[k] * f_inv[n-k]
    return res
