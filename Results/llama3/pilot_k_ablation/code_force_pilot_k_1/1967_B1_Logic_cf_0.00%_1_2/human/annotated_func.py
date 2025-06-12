#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two positive integers n and m, such that 1 <= n, m <= 2 * 10^6.
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: `t` is 0, `T` is equal to the initial value of `t`, `n` and `m` are the last two integers read from stdin, `ans` is the sum of `n // b + 1` for all `b` in the range from 1 to the minimum of `n` and `m` (inclusive) for the last test case, and this sum has been printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. For each test case, it calculates the sum of n // b + 1 for all b in the range from 1 to the minimum of n and m (inclusive), and prints this sum. The function iterates over all test cases and prints the calculated sum for each case.

