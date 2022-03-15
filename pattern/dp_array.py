
M = 4
N = 3
P = 2

# 1D
dp = [0]*N
print(f'1 * {N} ')
print(dp)

# 2D
dp = [[0]*N for _ in range(M)]
print(f'{M} * {N} ')
print(dp)

# 3D
print(f'{M} * {N} * {P}')
dp = [[[0]*P for _ in range(N)]for _ in range(M)]
print(dp)

# for m in dp:
#     print('m')
#     for n in m:
#         print('n')
#         print(n)
