for _ in range(int(input())):
    (n, k) = list(map(int, input().split(' ')))
    if n == k:
        print(('1 ' * n)[:-1])
    else:
        print(-1)