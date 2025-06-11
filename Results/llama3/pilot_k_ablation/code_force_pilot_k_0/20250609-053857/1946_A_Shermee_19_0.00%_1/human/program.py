t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    median_index = n // 2
    median = a[median_index]
    operations = 0
    for i in range(n):
        if a[i] < median:
            operations += median - a[i]
    print(operations)