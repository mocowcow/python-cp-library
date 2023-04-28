
def heapify(h):
    # a complete binary tree
    # has x non-leaf nodes and x+1 nodes
    # so we start from index size/2-1
    size = len(h)
    for i in reversed(range(size//2)):
        siftdown(h, i)


def push(h, x):
    # append a new node
    # then do siftup from new node
    h.append(x)
    size = len(h)
    siftup(h, size-1)


def pop(h):
    # swap root and the last node
    # delete the last node
    # then do siftdown from new root
    t = h[0]
    h[0] = h[-1]
    h.pop()
    siftdown(h, 0)
    return t


def siftup(h, i):
    # swap two nodes if child lesser than parent
    while i > 0:
        fa = (i-1)//2
        if h[i] < h[fa]:
            h[i], h[fa] = h[fa], h[i]
        i = fa


def siftdown(h, i):
    # find smallest children and swap with current node
    size = len(h)
    while i*2+1 < size:
        j = i*2+1
        if j+1 < size and h[j+1] < h[j]:
            j = j+1
        if h[j] < h[i]:
            h[i], h[j] = h[j], h[i]
        i = j
