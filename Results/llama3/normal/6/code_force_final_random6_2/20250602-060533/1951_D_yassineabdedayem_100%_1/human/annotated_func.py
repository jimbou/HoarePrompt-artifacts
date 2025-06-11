#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two positive integers n and k (1 <= n, k <= 10^18).
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: `t` is 0, `_` is `t`, `n` and `k` are the values from the last line of stdin, stdin is empty. If `n` equals `k`, 'YES' is printed, followed by the number 1 printed `t` times. If `n` is not equal to `k`, then if `n + 2` is greater than `k * 2`, 'YES' is printed, followed by the number 2 printed `t-1` times, the difference between `n` and `k` plus 1 printed `t-1` times, and finally the number 1 printed `t` times. Otherwise, 'NO' is printed `t` times.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of two positive integers n and k. It then determines whether it is possible to satisfy a certain condition based on the values of n and k. If n equals k, it prints 'YES' followed by the number 1. If n does not equal k, it checks if n + 2 is greater than k * 2. If this condition is true, it prints 'YES', followed by the number 2, the difference between n and k plus 1, and finally the number 1. If neither of these conditions is true, it prints 'NO'. The function repeats this process for each test case.

