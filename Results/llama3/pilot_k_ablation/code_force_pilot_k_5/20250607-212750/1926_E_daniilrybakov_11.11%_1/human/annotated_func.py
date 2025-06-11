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
        
    #State: t is an integer (1 <= t <= 5 * 10^4) and t is greater than or equal to 0, _ is t - 1, m is 2^x, k is an integer (1 <= k <= n_back <= 10^9) and k is greater than (n_back + 1) // 2 + (n_back + 1) // 4 + ... + 1, if n is 0, then s is equal to n_back and n is 1, otherwise s is less than k and n is (n_back + 1) // 2^x, stdin contains 0 lines, and a multiple of 2^x, where the multiple is less than or equal to 2 * k - 1, has been printed t times.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints a multiple of 2^x, where x is a non-negative integer, and the multiple is less than or equal to 2 * k - 1. The function repeats this process for each test case, and once all test cases have been processed, it terminates, leaving the standard input empty.

