#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t (1 <= t <= 1000). Each of the following t lines contains two positive integers n and k (1 <= n, k <= 10^18).
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
        
    #State: `_` is `t`, `t` is a positive integer between 1 and 1000, `n` and `k` are integers assigned from the input, stdin contains at least `t - 1` lines of input. If `n` equals `k`, 'YES' is printed, followed by the number 1. If `n` is not equal to `k`, then if `n + 2` is larger than `k * 2`, 'YES' is printed, followed by the number 2, the difference between `n` and `k` plus 1, and the number 1. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the results. It accepts a positive integer t (1 <= t <= 1000) and t pairs of positive integers n and k (1 <= n, k <= 10^18) as input. For each test case, it checks the relationship between n and k, and prints 'YES' or 'NO' accordingly. If 'YES', it also prints additional information: 1 if n equals k, or 2 followed by the difference between n and k plus 1 and 1 if n + 2 is larger than k * 2. The function processes all test cases and prints the results for each case.

