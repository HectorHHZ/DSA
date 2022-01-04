def MAXIMUM(a, l, r):
    if (r - l == 0):
        return a[r - 1]
    lmax = MAXIMUM(a, l, int((l + r)/2))
    rmax = MAXIMUM(a, int((l + r)/2) + 1, r)
    print(rmax, lmax)
    if rmax < lmax:
        return lmax
    else: return rmax




if __name__ == '__main__':
    MAXIMUM([10, 8, 6, 4, 2], 1, 5)