#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a positive integer t (1 <= t <= 10^4). Each test case contains two positive integers n and m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: `t` is a positive integer between 1 and 10^4, `T` is `t`, `stdin` is empty, `n` and `m` are the last two positive integers read from `stdin`, `ans` is the sum of `n // b + 1` for all `b` from 1 to `min(n, m)`, `b` is `min(n, m)`, and the sum of `n // b + 1` for all `b` from 1 to `min(n, m)` has been printed for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates the sum of n // b + 1 for all b from 1 to the minimum of n and m, and prints this sum for each test case. The function does not return any value, but rather prints the results for all test cases.

