#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) <= k:
            print('NO')
        else:
            print('Yes')
        
    #State: `t` is an integer between 1 and 1000, stdin is empty, `itest` is `t`, `n`, `m`, and `k` are the last values read from stdin, which are integers between 1 and 50. The output contains `t` lines, each containing either 'NO' or 'Yes', depending on the conditions `n <= k` or `n - math.ceil(n / m) <= k` for each input line.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of three integers: n, m, and k. It then determines whether a certain condition is met for each case, printing 'Yes' if the condition is met and 'NO' otherwise. The condition is that the number of elements (n) is greater than k and the number of elements minus the ceiling of n divided by m is also greater than k. The function processes all test cases and prints the corresponding results.

