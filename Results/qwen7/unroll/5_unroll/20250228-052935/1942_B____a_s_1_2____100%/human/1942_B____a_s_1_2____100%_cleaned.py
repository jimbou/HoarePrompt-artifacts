t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p = [-1] * n
    mex = n
    for i in range(n - 1, -1, -1):
        p[i] = mex - a[i]
        mex = min(mex, p[i])
    print(*p)