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
        
    #State: The output state will contain t lines, each containing a single integer. The integer on each line will be the result of the calculation (2 * (k - s) - 1) * m for the corresponding input values of n and k. The values of t, n, and k will remain unchanged.

#Overall this is what the function does:This function reads a series of input values from standard input, where the first line contains an integer t representing the number of test cases, followed by t lines each containing two integers n and k. For each test case, it calculates a result based on the values of n and k, and prints the result to standard output. The function does not modify the input values of t, n, or k. The output consists of t lines, each containing a single integer representing the calculated result for the corresponding input values of n and k.

