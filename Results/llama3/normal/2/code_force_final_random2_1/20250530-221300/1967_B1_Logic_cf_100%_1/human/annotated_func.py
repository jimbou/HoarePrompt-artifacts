#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: `t` is a positive integer that is at least 1, `T` is equal to `t`, `ans` is equal to `n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1))`, `n` is a positive integer, `m` is a positive integer that is at least 2, `b` is equal to `min(n, m) + 1`, stdin contains no test cases, and the value of `ans` is being printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains two positive integers n and m. It calculates a value 'ans' for each test case, which is the sum of n and the number of integers from 2 to the minimum of n and m that divide n with a remainder of b-1, where b is the divisor. The function then prints the calculated 'ans' value for each test case.

