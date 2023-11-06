

"""
單點更新
區間查詢

根節點id = 1，左節點 = id*2，.右節點 = id*2+1

設線段樹大小為N，最差情況需要4N空間保存節點
根節點代表區間[0, N-1]的答案

- 查詢區間[i, j]
query(1, 0, N-1, i, j)

- 對索引i增加val
update(1, 0, N-1, i, val)

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
    if i <= L and R <= j:  # 當前區間目標範圍包含
        return tree[id]
    ans = 0
    M = (L+R)//2
    if i <= M:
        ans += query(id*2, L, M, i, j)
    if M+1 <= j:
        ans += query(id*2+1, M+1, R, i, j)
    return ans


def update(id, L, R, i, val):
    """
    單點更新
    對索引i增加val
    """
    if L == R:  # 當前區間目標範圍包含
        tree[id] += val
        return
    M = (L+R)//2
    if i <= M:
        update(id*2, L, M, i, val)
    else:
        update(id*2+1, M+1, R, i, val)
    tree[id] = tree[id*2]+tree[id*2+1]  # 以左右子樹更新答案


N = 10**5
tree = [0]*(N*4)
# 將init設為初始值
init = [1]*N
build(1, 0, N-1)
