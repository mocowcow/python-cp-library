
"""
鴿巢原理
在有限格子內填入元素，盡可能保證相鄰元素不同

---

設最多元素 = a，有 MX 個。設總格子數 = S。
在保證相鄰不同的情況下，最多能放幾個 a？

1. 從奇偶性考慮
放一個 a、然後再放一個不同的，a 都會放到偶數位。
如果偶數位放完，繼續放 a 到奇數位就會衝突。

共有 ceil(S/2) 個偶數位：
- MX > ceil(S/2)，放不完，只能放 (S - MX) + 1 個。
- MX <= ceil(S/2)，可放完 MX 個。

2. 從間隔元素個數考慮
有 S - MX 個不同元素可以用做兩個 a 之間的間隔。
第一個 a 不需間隔，之後每個間隔可以多放一個。S - MX 個間隔可以放 (S - MX) + 1 個 a。  
- MX > (S - MX) + 1，放不完。只能放 (S - MX) + 1 個。
- MX <= (S - MX) + 1，可放完 MX 個。

---

式子一 MX > ceil(S/2)
式子二 MX > (S - MX) + 1

其實兩者是等價的，用哪個判斷都行。
MX > ceil(S/2)，展開上取整
MX > (S+1) / 2，同乘 2
2MX > S + 1，移項
MX > S - MX + 1

"""


# LC 767 (構造具體方案) https://leetcode.com/problems/reorganize-string/
# LC 1953 https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/
# LC 3495 https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
# CF 1907C https://codeforces.com/problemset/problem/1907/C
# CF 2003C (構造具體方案) https://codeforces.com/contest/2003/problem/C


# 元素 i 有 cnt[i] 個
# 保證相鄰元素不同，最多能放幾個元素
def can_put(cnt):
    S = sum(cnt)
    MX = max(cnt)

    if MX > (S+1) // 2:
        # 放不完
        # 只能放 (S - MX) 個最多元素
        # 加上 (S - MX) + 1 個其他元素
        # 共 (S - MX) * 2 + 1
        return (S - MX) * 2 + 1
    else:
        # 可全放完
        return S


# 構造具體放置方案
# 重組字串 s，使相鄰元素不相同
# 先填偶數格子，填完才填奇數格子
# 註：也可 max heap 或 sorted list 維護剩餘最大值，從頭依序填入
def try_fill(s):
    from collections import Counter
    cnt = Counter(s)
    pairs = cnt.most_common()  # 按照出現次數遞減排序

    S = len(s)  # 總個數
    MX = pairs[0][1]  # 最大出現次數

    # 最大的超過一半
    # if MX > (S + 1) // 2:
    if MX > (S - MX) + 1:
        return ""

    ans = [None] * S
    i = 0  # 先填偶數位
    for k, v in pairs:
        for _ in range(v):
            ans[i] = k
            i += 2
            if i >= S:  # 偶數填完，填奇數位
                i = 1

    return "".join(ans)
