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
        
    #State: `t` is an integer between 0 and 997 (inclusive), `n` and `k` are the positive integers from the last line of stdin, `_` is `t`, stdin contains 0 lines. If `n` equals `k`, 'YES' is printed, and 1 is printed twice. If `n` is not equal to `k`, and `n + 2` is greater than `k * 2`, 'YES' is printed, followed by 2, the difference between `n` and `k` plus 1, and finally 1. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two positive integers n and k. It then determines whether it's possible to satisfy a certain condition based on the values of n and k. If n equals k, it prints 'YES' followed by 1 twice. If n is not equal to k but n + 2 is greater than k * 2, it prints 'YES', 2, the difference between n and k plus 1, and 1. Otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results.

