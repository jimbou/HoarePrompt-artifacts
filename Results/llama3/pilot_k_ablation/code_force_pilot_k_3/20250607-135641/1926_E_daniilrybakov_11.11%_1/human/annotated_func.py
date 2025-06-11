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
        
    #State: t is 0, _ is t, n_back is an integer, s is equal to n_back if n is 0, otherwise s is equal to k, m is 2^x where x is the number of iterations, n is 0, stdin contains no input, k is an integer, and this is printed: (2 * (k - (s - n)) - 1) * m, where s is equal to n_back and m is 2^x

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints a value based on these inputs, specifically (2 * (k - (s - n)) - 1) * m, where s and m are determined through a loop that iterates until s is greater than or equal to k. The function processes all test cases and prints the calculated values for each case.

