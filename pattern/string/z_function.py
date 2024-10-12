
# LCP (Longest Common prefix)：最長公共前綴
# s[i..]：以 s[i] 開頭的後綴
# 定義 z[i] = LCP(s, s[i..])
# z[0] 即字串 s 與自身匹配，不具意義。特別約定 z[i] = 0


# 文本與後綴求 LCP
# LC2223 https://leetcode.com/problems/sum-of-scores-of-built-strings/
# LC3031 https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/
# LC3045 https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/


# 文本 s 與模式 p 串接，做字串查找
# LC3008 https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/
# LC3034 https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/
# LC3303 https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/


def z_function(s):
    N = len(s)
    z = [0]*N
    L = R = 0
    for i in range(1, N):
        if R < i:  # not covered by previous z-box
            # z[i] = 0
            pass
        else:  # partially or fully covered
            j = i-L
            if j+z[j] < z[L]:  # fully covered
                z[i] = z[j]
            else:
                z[i] = R-i+1

        while i+z[i] < N and s[i+z[i]] == s[z[i]]:  # remaining substring
            z[i] += 1
        if i+z[i]-1 > R:  # R out of prev z-box, update R
            L = i
            R = i+z[i]-1

    return z


s = 'abaabaab'
print(z_function(s))
