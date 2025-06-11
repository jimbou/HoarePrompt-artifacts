#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains 3 integers n, m and k, followed by m lines each containing three integers a_i, b_i, f_i. n is an integer such that 2 <= n <= 10^5, m is an integer such that 0 <= m <= min(10^5, n(n-1)/2), k is an integer such that 1 <= k <= 2 * 10^5. a_i and b_i are integers such that 1 <= a_i, b_i <= n and a_i != b_i. f_i is an integer such that 1 <= f_i <= 10^9.
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
        
    #State: The loop has executed t times, and for each execution, it has read m lines of input, calculated the sum of f values, and printed the result of the modular inverse calculation. The values of n, m, k, sum_f, cn2, p, q, and gcd have been updated accordingly for each iteration. The final output state is the result of the last iteration, with the values of n, m, k, sum_f, cn2, p, q, and gcd reflecting the last test case processed. The value of t remains unchanged, as it is the loop counter. The value of M remains unchanged, as it is a constant. The stdin has been consumed by the loop, and its contents are no longer available.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers (n, m, k) followed by m lines of three integers (a, b, f). It calculates the sum of f values for each test case, then computes the modular inverse of a value derived from n, m, k, and the sum of f values. The function prints the result of the modular inverse calculation for each test case. The function consumes all input from standard input and produces output for each test case.

