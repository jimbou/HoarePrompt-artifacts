#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains 3 integers n, m and k, followed by m lines, each containing three integers a_i, b_i, f_i. n is the number of children, m is the number of pairs of friends, and k is the number of excursions. a_i and b_i are the indices of the pair of children who are friends, and f_i is their friendship value. 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2*10^5, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9.
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
        
    #State: t is greater than or equal to 0, i is t-1, M is 1000000007, n is an integer, m is an integer and must be equal to 0, k is an integer, j is m-1, sum_f is equal to the original sum_f plus the sum of all the third integers from all the inputs, a is an integer equal to the first integer from the last input, b is an integer equal to the second integer from the last input, f is an integer equal to the third integer from the last input, stdin contains multiple test cases minus m, cn2 is n*(n-1)/2, p is (2*k*cn2*sum_f + m*k*(k-1)) divided by the greatest common divisor of p and q, q is (n*(n-1)/2)^2 divided by the greatest common divisor of p and q, and the value of p multiplied by the modular multiplicative inverse of q modulo M is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers n, m, and k, followed by m lines of three integers a_i, b_i, and f_i. It calculates the sum of all f_i values, then computes two values p and q based on n, m, k, and the sum of f_i. The function then prints the modular multiplicative inverse of q modulo M (where M is 10^9 + 7) multiplied by p, for each test case.

