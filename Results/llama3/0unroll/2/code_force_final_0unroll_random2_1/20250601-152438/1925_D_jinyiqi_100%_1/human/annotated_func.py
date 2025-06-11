#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains multiple lines. The first line contains three integers: n, m, and k. The next m lines contain three integers each: a_i, b_i, and f_i. The input is well-formed, and the constraints on the input values are met: 1 <= t <= 5 * 10^4, 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2 * 10^5, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9.
    t = int(input())
    M = 10 ** 9 + 7
    for i in range(t):
        n, m, k = map(int, input().split())
        
        sum_f = 0
        
        for j in range(m):
            a, b, f = map(int, input().split())
            sum_f += f
        
        cn2 = n * (n - 1) // 2
        
        p = 2 * k * cn2 * sum_f + m * k * (k - 1)
        
        q = 2 * cn2 ** 2
        
        gcd = math.gcd(p, q)
        
        p = p // gcd
        
        q = q // gcd
        
        print(int(p * pow(q, -1, M) % M))
        
    #State: Output State: The loop has executed t times, and for each execution, it has read m lines of input from stdin, calculated and printed the modular inverse of a fraction, and updated the values of variables p, q, and gcd. The final state of the variables is: t is unchanged, M is unchanged, stdin contains no more lines, n, m, k, sum_f, cn2, p, q, and gcd have been updated to their values from the last iteration of the loop.

#Overall this is what the function does:Calculates and prints the modular inverse of a fraction for each of t test cases, where the fraction is derived from the input values n, m, k, and the sum of f values, and the modulus is 10^9 + 7. The function reads input from stdin, processes it, and outputs the results, leaving the input stream empty after execution.

