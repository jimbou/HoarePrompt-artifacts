def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
    return True

def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and (list[i + 1] > 0):
            list[i + 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i - 1] -= 1 * list[i - 1]
        if list[i - 1] != 0:
            print('no')
            return
    if func_1(list, n):
        print('YES')
    else:
        print('NO')
t = int(input())
for i in range(t):
    n = int(input())
    l = input()
    lst = list(map(int, l.split()))
    func_2(lst, n)