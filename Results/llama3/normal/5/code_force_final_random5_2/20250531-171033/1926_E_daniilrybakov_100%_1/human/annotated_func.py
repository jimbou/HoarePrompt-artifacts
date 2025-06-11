#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5 * 10^4) followed by t lines, each containing two integers n and k (1 <= k <= n <= 10^9).
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        s = 0
        
        m = 1
        
        while n:
            x = (n + 1) // 2
            n //= 2
            if s < k and k <= s + x:
                break
            s += x
            m *= 2
        
        print((2 * (k - s) - 1) * m)
        
    #State: t is an integer greater than or equal to 0, _ is t, n is 0, k is an integer, s is the sum of the original values of n, m is a power of 2, and this is printed: (2 * (k - s) - 1) * m

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and k. It then calculates and prints the result of a specific mathematical operation for each test case. The operation involves finding the sum of the original values of n, determining a power of 2, and using these values to compute a final result. The function processes all test cases and prints the corresponding results.

