for s in [*open(0)][1:]:
    (n, k) = map(int, s.split())
    if k >= 2:
        if n == k:
            print(*[k for j in range(k)])
        else:
            print('-1')
    else:
        print(*[j for j in range(n)])