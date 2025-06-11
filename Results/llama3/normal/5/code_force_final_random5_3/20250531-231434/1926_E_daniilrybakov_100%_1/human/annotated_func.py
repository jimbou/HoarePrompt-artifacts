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
        
    #State: t is 0, _ is t, stdin contains 0 lines, n is 0, k is an integer, s is equal to its original value plus the sum of x in each iteration, m is equal to its original value times 2 to the power of the number of iterations, and this is printed: (2 * (k - s) - 1) * m

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints the result of a specific formula, (2 * (k - s) - 1) * m, for each test case. The function iterates through each test case, updating variables n, k, s, and m according to the given formula, until all test cases have been processed. The final state of the program is that all test cases have been processed, and the corresponding results have been printed.

