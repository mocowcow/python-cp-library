

# 輸入 --------------------------------------------------

# 讀一個 int
arg = int(input())

# 讀多個 int
arg1, arg2 = map(int, input().split())

# 讀 int 陣列
arr = map(int, input().split())

# 讀取 t 個測資
t = int(input())
for _ in range(t):
    pass


# 輸出 --------------------------------------------------

# 空白分隔符 輸出整數陣列
ans = [1, 2, 3]
print(" ".join(map(str, ans)))
