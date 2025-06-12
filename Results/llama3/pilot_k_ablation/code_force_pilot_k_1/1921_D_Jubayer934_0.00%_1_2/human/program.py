import math
n = int(input())
for i in range (n):
    m,n = map(int, input().split())
    a = list(map(int,input().split()))[:m]
    b = list(map(int,input().split()))[:n]
    b.sort()
    result = []
 
    n = n//2
 
    for i in range (len(a)):
        if len(a) == len(b):
            break
        b.remove(b[n-1])
    for i in range (len(a)):
        result.append(abs(max(a) - min(b)))
        a.remove(max(a))
        b.remove(min(b))
    print(sum(result))