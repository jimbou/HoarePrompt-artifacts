#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two integers n, m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: `t` is an integer between 1 and 10^4 (inclusive), `T` is `t`, `n` is an integer between 1 and 2 * 10^6 (inclusive), `m` is an integer between 1 and 2 * 10^6 (inclusive), `ans` is the sum of `n // b + 1` for all `b` from 1 to `min(n, m)`, `stdin` is empty, `b` is `min(n, m)`, and the sum of `n // b + 1` for all `b` from 1 to `min(n, m)` which is equal to `ans` has been printed for all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and m. It calculates the sum of the integer division of n by all numbers from 1 to the minimum of n and m, adds 1 to each result, and then prints this sum for each test case. The function processes all test cases and empties the standard input.

