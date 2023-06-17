

# precompute all factorial and modular multiplicative inverse for factorial
# O(MX log EXP) where EXP = MOD-2
MOD = 10**9+7
MX = 10
f = [0]*(MX+1)
finv = [0]*(MX+1)
f[0] = finv[0] = 1
f[1] = finv[1] = 1
for i in range(2, MX+1):
    f[i] = (f[i-1]*i) % MOD
    finv[i] = pow(f[i], -1, MOD)


# linear version
# O(MX)
MOD = 10**9+7
MX = 10**5
f = [0]*(MX+1)
inv = [0]*(MX+1)
finv = [0]*(MX+1)
f[0] = inv[0] = finv[0] = 1
f[1] = inv[1] = finv[1] = 1
for i in range(2, MX+1):
    f[i] = (f[i-1]*i) % MOD
    inv[i] = (MOD-MOD//i)*inv[MOD % i] % MOD
    finv[i] = finv[i-1]*inv[i] % MOD
