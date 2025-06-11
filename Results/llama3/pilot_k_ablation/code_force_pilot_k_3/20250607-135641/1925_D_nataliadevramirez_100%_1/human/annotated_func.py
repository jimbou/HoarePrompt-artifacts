#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains 3 integers n, m and k, followed by m lines, each containing three integers a_i, b_i, f_i. 1 <= t <= 5 * 10^4, 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2 * 10^5, 1 <= a_i, b_i <= n, a_i != b_i, 1 <= f_i <= 10^9.
    MOD = 1000000007
    T = int(input())
    for _ in range(T):
        n, p, k = map(int, input().split())
        
        S = 0
        
        for i in range(p):
            S += int(input().split()[2])
        
        C = n * (n - 1) // 2
        
        num = p * k * k - p * k + 2 * k * C * S
        
        den = 2 * C * C
        
        g = math.gcd(num, den)
        
        num = num // g
        
        den = den // g
        
        den = pow(den, -1, MOD)
        
        ans = num * den % MOD
        
        print(ans)
        
    #State: T is 0, _ is T, MOD is 1000000007, n is the first integer in the input, p is the second integer in the input and must be greater than or equal to 0, k is the third integer in the input, S is the sum of the third integer in the input and the previous value of S, i is p, C is n*(n-1)/2, num is (p*k*k-p*k+2*k*C*S)/(2*C*C), den is the modular multiplicative inverse of 2*C*C modulo MOD, ans is (num*den) % MOD, g is the greatest common divisor of (p*k*k-p*k+2*k*C*S) and (2*C*C), and stdin contains multiple test cases minus p, and ans is printed, ans (where ans is the result of the expression (num*den) % MOD, and num is (p*k*k-p*k+2*k*C*S)/(2*C*C), den is the modular multiplicative inverse of 2*C*C modulo MOD)

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing three integers n, m, and k, followed by m lines of three integers a_i, b_i, and f_i. It calculates a value based on these inputs using modular arithmetic and prints the result for each test case. The function performs the following actions: reads input, calculates the sum of the third integer in each line, computes the value of C as n*(n-1)/2, calculates the numerator and denominator of a fraction, reduces the fraction by dividing both numerator and denominator by their greatest common divisor, calculates the modular multiplicative inverse of the denominator, multiplies the numerator by the modular multiplicative inverse of the denominator, takes the result modulo MOD, and prints the final result for each test case.

