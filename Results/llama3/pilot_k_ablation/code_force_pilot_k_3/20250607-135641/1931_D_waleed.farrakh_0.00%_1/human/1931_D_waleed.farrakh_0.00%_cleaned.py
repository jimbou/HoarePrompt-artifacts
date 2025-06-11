def func_1(test_cases):
    results = []
    for (n, x, y, arr) in test_cases:
        count = 0
        mod_x = {}
        mod_y = {}
        for num in arr:
            rem_x = -num % x
            rem_y = num % y
            count += mod_x.get(rem_x, 0) and mod_y.get(rem_y, 0)
            mod_x[num % x] = mod_x.get(num % x, 0) + 1
            mod_y[num % y] = mod_y.get(num % y, 0) + 1
        results.append(count)
    return results

def func_2():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    test_cases = []
    idx = 1
    for _ in range(t):
        (n, x, y) = map(int, data[idx].split())
        arr = list(map(int, data[idx + 1].split()))
        test_cases.append((n, x, y, arr))
        idx += 2
    results = func_1(test_cases)
    for result in results:
        print(result)
if __name__ == '__main__':
    func_2()