from collections import deque


# 將不重複出現的小寫字母轉成bit mask
def lower_as_mask(s):
    n = 0
    for c in s:
        n |= 1 << (ord(c)-97)
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


# graph每個節點訪問狀態以mask表示
# 求走完所有點的最短步數
def graph_as_mask(N):
    N = 3
    end = (1 << N)-1
    visited = set()
    step = 0
    q = deque([(0, 0)])
    while q:
        for _ in range(len(q)):
            curr, mask = q.popleft()
            mask |= (1 << curr)
            if mask == end:  # 全部走完
                return step
            visited.add(curr, mask)
            # 往鄰接點bfs
            pass
        step += 1
