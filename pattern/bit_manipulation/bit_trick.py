from collections import Counter


def bit_trick(nums):
    d = Counter()
    op_res = []  # [subarray res, first index, last index]
    for i, x in enumerate(nums):
        op_res.append([x, i, i])
        tail = 0
        for v in op_res:
            v[0] |= x
            if op_res[tail][0] != v[0]:
                tail += 1
                op_res[tail] = v
            else:
                op_res[tail][2] = v[2]
        del op_res[tail + 1:]  # op_res = op_res[:tail + 1]

        # update frequency
        for val, mn, mx in op_res:
            d[val] += mx - mn + 1
    return d
