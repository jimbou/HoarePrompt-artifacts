#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m, and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `itest` is `t-1`, `n`, `m`, and `k` are assigned the values of the last line of input from stdin, stdin is empty. If `n` is less than or equal to `k` or `n` minus the ceiling of `n` divided by `m` is less than `k`, 'NO' is printed. Otherwise, 'Yes' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers n, m, and k. It then determines whether a certain condition is met, specifically whether n is greater than k and n minus the ceiling of n divided by m is also greater than k. If the condition is met, it prints 'Yes', otherwise it prints 'NO'. The function processes multiple test cases and prints the result for each case.

