

"""
區間更新
區間查詢

根節點id = 1，左節點 = id*2，.右節點 = id*2+1

設線段樹大小為N，最差情況需要4N空間保存節點
根節點代表區間[0, N-1]的答案

- 區間查詢[i, j]
query(1, 0, N-1, i, j)

- 區間更新[i, j]每個索引加上val
update(1, 0, N-1, i, j, val)

"""


def build(id, L, R):
    """
    初始化線段樹
    若無初始值則不需執行
    """
    if L == R:  # 到達葉節點
        tree[id] = init[L]
        return
    M = (L+R)//2
    build(id*2, L, M)
    build(id*2+1, M+1, R)
    tree[id] = tree[id*2]+tree[id*2+1]  # 以左右子樹更新答案


def query(id, L, R, i, j):
    """
    區間查詢
    回傳[i, j]的總和
    """
    if i <= L and R <= j:  # 當前區間被目標範圍包含
        return tree[id]
    push_down(id, L, R)
    ans = 0
    M = (L+R)//2
    if i <= M:
        ans += query(id*2, L, M, i, j)
    if M+1 <= j:
        ans += query(id*2+1, M+1, R, i, j)
    return ans


def update(id, L, R, i, j, val):
    """
    區間更新
    對[i, j]每個索引都增加val
    """
    if i <= L and R <= j:  # 當前區間被目標範圍包含
        tree[id] += (R-L+1)*val
        lazy[id] += val  # 標記每個位置都加val
        return
    push_down(id, L, R)
    M = (L+R)//2
    if i <= M:
        update(id*2, L, M, i, j, val)
    if M+1 <= j:
        update(id*2+1, M+1, R, i, j, val)
    push_up(id)


def push_down(id, L, R):
    """
    將區間懶標加到答案中
    下推懶標記給左右子樹
    """
    M = (L+R)//2
    if lazy[id]:
        lazy[id*2] += lazy[id]
        tree[id*2] += lazy[id]*(M-L+1)
        lazy[id*2+1] += lazy[id]
        tree[id*2+1] += lazy[id]*(R-(M+1)+1)
        lazy[id] = 0


def push_up(id):
    """
    以左右子樹更新答案
    """
    tree[id] = tree[id*2]+tree[id*2+1]


N = 5
tree = [0]*(N*4)
lazy = [0]*(N*4)

# 將init設為初始值
init = [1]*N
build(1, 0, N-1)

# [1,1,1,1,1]
print(query(1, 0, N-1, 1, 1))  # 1
update(1, 0, N-1, 0, 4, 2)  # [3,3,3,3,3]
print("----")
print(query(1, 0, N-1, 1, 1))  # 3
print(query(1, 0, N-1, 0, 4))  # 15
update(1, 0, N-1, 0, 2, 3)  # [6,6,6,3,3]
print("----")
print(query(1, 0, N-1, 0, 0))  # 6
print(query(1, 0, N-1, 1, 1))  # 6
print(query(1, 0, N-1, 2, 2))  # 6
print(query(1, 0, N-1, 3, 3))  # 3
print(query(1, 0, N-1, 4, 4))  # 3
update(1, 0, N-1, 1, 3, -3)  # [6,3,3,0,3]
update(1, 0, N-1, 0, 1, 2)  # [8,5,3,0,3]
print("----")
print(query(1, 0, N-1, 0, 0))  # 8
print(query(1, 0, N-1, 1, 1))  # 5
print(query(1, 0, N-1, 2, 2))  # 3
print(query(1, 0, N-1, 3, 3))  # 0
print(query(1, 0, N-1, 4, 4))  # 3
print(query(1, 0, N-1, 0, 2))  # 16
print(query(1, 0, N-1, 2, 3))  # 3
print(query(1, 0, N-1, 2, 4))  # 6
