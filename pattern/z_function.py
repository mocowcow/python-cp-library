

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
