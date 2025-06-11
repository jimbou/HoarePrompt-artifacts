t = int(input())
l = 0
h = 0
for i in range(t):
    a = str(input())
    for j in a:
        if j in 'A':
            l += 1
        else:
            h += 1
    if l > h:
        print('A')
    elif l < h:
        print('B')