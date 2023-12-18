
# 生成回文數
# 枚舉左半邊，反轉成為右半邊
# 如果上限長度為n，則左半長度只需枚舉到n/2

pa = []
for x in range(1, 10):
    pa.append(x)

for x in range(1, 10000):
    # even: x+x
    left = right = x
    while right > 0:
        right, r = divmod(right, 10)
        left = left*10+r
    pa.append(left)

    # odd: x+mid+x
    for mid in range(10):
        left = x*10+mid
        right = x
        while right > 0:
            right, r = divmod(right, 10)
            left = left*10+r
        pa.append(left)

pa.sort()
