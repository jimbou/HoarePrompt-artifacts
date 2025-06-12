#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        n_back = n
        
        s = (n + 1) // 2
        
        n = (n + 1) // 2
        
        m = 1
        
        while s < k:
            if n == 0:
                s = n_back
                n = 1
                break
            m *= 2
            n //= 2
            s += n
        
        print((2 * (k - (s - n)) - 1) * m)
        
    #State: `t` is 0, stdin is empty, `m`, `n`, `n_back`, `s` are not defined, and `t` lines have been printed, each containing a calculated value based on the input values `n` and `k`.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains an integer `t` representing the number of test cases, and each subsequent line contains two integers `n` and `k`. For each test case, it calculates a value based on `n` and `k` using a while loop and prints the result. The function continues this process until all `t` test cases have been processed, at which point it leaves the input stream empty and the variables `m`, `n`, `n_back`, and `s` undefined. The function's primary purpose is to perform calculations and print results for multiple test cases based on input values.

