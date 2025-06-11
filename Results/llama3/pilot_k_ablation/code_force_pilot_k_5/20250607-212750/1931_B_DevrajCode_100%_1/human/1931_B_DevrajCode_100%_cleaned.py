def func_1(n, a):
    total_water = sum(a)
    target = total_water // n
    if total_water % n != 0:
        return 'NO'
    container = 0
    for water in a:
        container += water - target
        if container < 0:
            return 'NO'
    return 'YES'
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(func_1(n, a))