

def print_mat(mat):
    for r in mat:
        print([x for x in r])
    print('---------')


def copy_mat(mat):
    return[list.copy(r) for r in mat]


def transpose(mat):
    return [list(r) for r in zip(*mat)]


def horizontal_flip(mat):
    # N = len(mat)
    # hori = copy_mat(mat)
    # for i in range(N):
    #     l, r = 0, N-1
    #     while l < r:
    #         hori[i][l], hori[i][r] = hori[i][r], hori[i][l]
    #         l, r = l+1, r-1
    # return hori
    return [r[::-1] for r in mat]


def vertical_flip(mat):
    # N = len(mat)
    # verti = copy_mat(mat)
    # l, r = 0, N-1
    # while l < r:
    #     verti[l], verti[r] = verti[r], verti[l]
    #     l, r = l+1, r-1
    # return verti
    return mat[::-1]


def right_90(mat):
    r90 = copy_mat(mat)
    r90 = transpose(r90)
    r90 = horizontal_flip(r90)
    return r90


def left_90(mat):
    l90 = copy_mat(mat)
    l90 = horizontal_flip(l90)
    l90 = transpose(l90)
    return l90


######################################################
######################################################


mat = [
    [1, 2, 9],
    [4, 5, 9],
    [7, 8, 9]
]

print('original mat')
print('原始矩陣')
print_mat(mat)

trans = transpose(mat)
print('mat transpose')
print('矩陣轉置')
print_mat(trans)

hori = horizontal_flip(mat)
print('mat horizontal flip')
print('水平翻轉')
print_mat(hori)

verti = vertical_flip(mat)
print('mat vertical flip')
print('垂直翻轉')
print_mat(verti)

r90 = right_90(mat)
print('mat right rotate 90')
print('向右轉90')
print_mat(r90)

l90 = left_90(mat)
print('mat left rotate 90')
print('向左轉90')
print_mat(l90)
