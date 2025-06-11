#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains multiple lines. The first line contains three integers: n, m, and k. The next m lines contain three integers each: a_i, b_i, and f_i. n is an integer between 2 and 10^5 (inclusive), m is an integer between 0 and min(10^5, n*(n-1)/2) (inclusive), k is an integer between 1 and 2*10^5 (inclusive), a_i and b_i are integers between 1 and n (inclusive), and f_i is an integer between 1 and 10^9 (inclusive).
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
        
    #State: t is an integer greater than or equal to 0, M is 1000000007, n is an integer between 2 and 10^5 (inclusive), m is an integer between 0 and min(10^5, n*(n-1)/2) (inclusive), k is an integer between 1 and 2*10^5 (inclusive), sum_f is the sum of all f values from the input, a is an integer, b is an integer, f is an integer, j is m, stdin contains multiple test cases minus one, each test case contains multiple lines minus one, cn2 is n*(n-1)/2, p is (2*k*cn2*sum_f + m*k*(k-1)) divided by the greatest common divisor of (2*k*cn2*sum_f + m*k*(k-1)) and (2*cn2^2), q is (2*cn2^2) divided by the greatest common divisor of (2*k*cn2*sum_f + m*k*(k-1)) and (2*cn2^2), gcd is the greatest common divisor of (2*k*cn2*sum_f + m*k*(k-1)) and (2*cn2^2), and the result of the modular arithmetic operation int(p * pow(q, -1, M) % M) is being printed, i is t-1, and this is printed: the result of the modular arithmetic operation int(p * pow(q, -1, M) % M) which is equal to int(((2*k*cn2*sum_f + m*k*(k-1)) / gcd) * pow((2*cn2^2)/gcd, -1, M) % M)

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing multiple lines. For each test case, it reads three integers (n, m, and k) and then m lines, each containing three integers (a, b, and f). It calculates the sum of all f values and uses this sum, along with n, m, and k, to compute two values (p and q) and their greatest common divisor (gcd). The function then prints the result of a modular arithmetic operation involving p, q, and gcd for each test case.

