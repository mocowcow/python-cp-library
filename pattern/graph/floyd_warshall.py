from math import inf
from collections import defaultdict


# array version
class FloydWarshall:
    def __init__(self, n):
        self.n = n
        self.dp = [[inf]*n for _ in range(n)]
        for i in range(n):
            self.dp[i][i] = 0

    def add(self, a, b, c):
        if c < self.dp[a][b]:
            self.dp[a][b] = c

    def get(self, a, b):
        return self.dp[a][b]

    def build(self):
        for k in range(self.n):
            for i in range(self.n):
                if self.dp[i][k] == inf:  # pruning
                    continue
                for j in range(self.n):
                    new_dist = self.dp[i][k]+self.dp[k][j]
                    if new_dist < self.dp[i][j]:
                        self.dp[i][j] = new_dist


# dict version
# can use string as key
class FloydWarshallDict:
    def __init__(self, vertexes):
        self.dp = defaultdict(lambda: defaultdict(lambda: inf))
        for v in vertexes:
            self.dp[v][v] = 0

    def add(self, a, b, c):
        if c < self.dp[a][b]:
            self.dp[a][b] = c

    def get(self, a, b):
        return self.dp[a][b]

    def build(self):
        for k in self.dp:
            for i in self.dp:
                if self.dp[i][k] == inf:  # pruning
                    continue
                for j in self.dp:
                    new_dist = self.dp[i][k]+self.dp[k][j]
                    if new_dist < self.dp[i][j]:
                        self.dp[i][j] = new_dist
