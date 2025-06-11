def func_1(s):
    ans = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i:i + 5] == 'mapie':
            ans += 1
            i += 5
        elif s[i:i + 3] == 'map':
            ans += 1
            i += 3
        elif s[i:i + 3] == 'pie':
            ans += 1
            i += 3
        else:
            i += 1
    return ans
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(func_1(s))