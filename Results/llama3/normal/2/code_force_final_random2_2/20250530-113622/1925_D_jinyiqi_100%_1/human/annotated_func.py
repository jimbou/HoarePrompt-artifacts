#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer k, followed by k lines, each containing three integers n, m, and k, followed by m lines, each containing three integers a_i, b_i, and f_i.
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
        
    #State: t is greater than or equal to 0, i is t, M is 1000000007, n is an integer, m is 0, k is an integer, sum_f is the original value of sum_f plus the sum of all f values from stdin, a is the first integer from stdin, b is the second integer from stdin, f is the last integer from stdin, j is m, stdin contains multiple test cases minus m, cn2 is n * (n - 1) // 2, p is (2 * k * cn2 * sum_f + m * k * (k - 1)) // gcd, q is (2 * cn2 squared) // gcd, gcd is the greatest common divisor of p and q, and the integer value of p * pow(q, -1, M) % M has been printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer k, followed by k lines of three integers each. It calculates a value based on these inputs and prints the result for each test case. The function performs the following actions: reads input, calculates the sum of certain values, computes the greatest common divisor of two values, and prints the result of a modular arithmetic operation. The function does not modify any input variables and does not have any side effects other than printing the results.

