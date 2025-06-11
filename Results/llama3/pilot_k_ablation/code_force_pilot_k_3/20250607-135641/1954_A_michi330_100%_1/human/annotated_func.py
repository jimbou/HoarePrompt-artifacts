#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is an integer and is at least 1, `itest` is `t-1`, `n`, `m`, `k` are integers and are assigned values from the input, stdin contains no input. If `n` is less than or equal to `k` or `n` minus the ceiling of `n` divided by `m` is less than or equal to `k`, then 'NO' is printed. Otherwise, 'Yes' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers: n, m, and k. It then determines whether a certain condition is met, specifically if n is less than or equal to k or if n minus the ceiling of n divided by m is less than or equal to k. If the condition is true, it prints 'NO', otherwise it prints 'Yes'. The function processes multiple test cases as specified by the initial input integer t, and it consumes all input from standard input, leaving it empty after execution.

