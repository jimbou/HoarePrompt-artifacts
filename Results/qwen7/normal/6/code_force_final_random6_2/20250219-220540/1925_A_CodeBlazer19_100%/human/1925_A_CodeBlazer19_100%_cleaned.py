t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    print('abcdefghijklmnopqrstuvwxyz'[:k] * n)