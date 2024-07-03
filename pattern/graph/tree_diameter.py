
"""

在無向樹狀圖中，直徑指的是樹中任意兩點之間的最長路徑長度。
注意：
- 直徑可能不只一條。  
- 邊權為負數時不適用。  

選擇任意出發點 start，透過 dfs/bfs 找到距離 start 最遠的節點 u。  
再次從 u 出發，dfs/bfs 找到距離 u 最遠的節點 v。  
(u, v) 即為直徑。  


為何 dfs/bfs 一定能找到構成直徑的節點？
證明：

樹狀圖可以任意調整形狀，故將起點 start 當作根節點，比較方便討論。  

設 (u, v) 為一直徑。  
d1 為 (start, u) 的距離，d2 為 (start, v) 的距離，且 d1 >= d2。

從任意點 start 做 dfs/bfs 找到節點 end。
case1：(start, end) 小於 d2。
根據 dfs 找最遠的邏輯，不可能找到比 d2 更近的點。  

case2：(start, end) 大於 d2。
若為真，則可以拿 end 取代 u, v 任一點，構成更長的路徑。
此結論與 (u, v) 為直徑的前提矛盾。

https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/solutions/2826761/3203-he-bing-liang-ke-shu-hou-de-zui-xia-ulhz/
https://oi-wiki.org/graph/tree-diameter/#%E5%81%9A%E6%B3%95-1-%E4%B8%A4%E6%AC%A1-dfs

"""

# LC 2303 https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
# LC 1245(會員題) https://leetcode.com/problems/tree-diameter/


def diameter_dfs(edges):
    N = len(edges) + 1
    g = [[] for _ in range(N)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    farthest = None
    mx_dist = -1

    def dfs(i, fa, dist):
        nonlocal farthest, mx_dist
        if dist > mx_dist:
            mx_dist = dist
            farthest = i
        for j in g[i]:
            if j == fa:
                continue
            dfs(j, i, dist + 1)

    dfs(0, -1, 0)

    mx_dist = -1
    dfs(farthest, -1, 0)
    return mx_dist


def diameter_bfs(edges):
    N = len(edges) + 1
    g = [[] for _ in range(N)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    def bfs(start):
        dist = [-1] * N
        dist[start] = 0
        q = [start]
        while q:
            q2 = []
            for i in q:
                for j in g[i]:
                    if dist[j] == -1:
                        dist[j] = dist[i] + 1
                        q2.append(j)
            q = q2

        farthest = None
        mx_dist = -1
        for i, d in enumerate(dist):
            if d > mx_dist:
                mx_dist = d
                farthest = i
        return farthest, mx_dist

    u, dist = bfs(0)
    v, dist = bfs(u)
    return dist
