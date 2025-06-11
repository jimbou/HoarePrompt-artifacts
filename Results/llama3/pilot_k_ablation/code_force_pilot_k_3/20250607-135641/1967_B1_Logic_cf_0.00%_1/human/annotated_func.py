#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: `t` is an integer between 1 and 10^4, `T` is `t-1`, `stdin` contains 0 lines of input, `n` and `m` are positive integers that must have a minimum value greater than or equal to `min(n, m)`, `ans` is `sum(n // b + 1 for b in range(1, min(n, m) + 1))`, `b` is `min(n, m)`, and the value of `ans` is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates the sum of the number of multiples of each integer from 1 to the minimum of n and m, and prints the result. The function processes all test cases and prints their corresponding results.

