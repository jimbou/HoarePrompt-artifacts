#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `itest` is `t`, `n`, `m`, and `k` are integers where 1 <= m, k <= n <= 50, stdin is empty. The program has printed 'NO' or 'Yes' for each of the `t` test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers n, m, and k. It then determines whether a certain condition is met (n > k and n - math.ceil(n / m) > k) and prints 'Yes' if the condition is true and 'NO' otherwise. The function processes multiple test cases and prints a result for each case.

