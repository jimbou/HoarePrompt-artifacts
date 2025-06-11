#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 10^4). Each test case contains two positive integers n, m (1 <= n, m <= 2 * 10^6).
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: t is at least 1, T is t - 1, n is a positive integer, m is a positive integer, ans is equal to n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1)), stdin contains multiple test cases - t, b is min(n, m), and the value of ans which is equal to n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1)) is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates a value 'ans' for each test case, which is initially set to n and then incremented by the sum of the integer divisions of (n + b) by (b * b) for all b from 2 to the minimum of n and m. The calculated 'ans' value for each test case is then printed to the standard output.

