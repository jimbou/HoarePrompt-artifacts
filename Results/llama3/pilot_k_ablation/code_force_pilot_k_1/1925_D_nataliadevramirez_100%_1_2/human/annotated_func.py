#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t (1 <= t <= 5 * 10^4) on the first line, followed by 3 integers n, m, and k (2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5) on the next line. Then, for each test case, there are m lines, each containing three integers a_i, b_i, and f_i (a_i != b_i, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9).
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
        
    #State: T is an integer between 1 and 5 * 10^4, MOD is 1000000007, _ is T, stdin contains T less inputs, and T times ans is printed

#Overall this is what the function does:The function reads multiple test cases from standard input, each containing an integer t, followed by 3 integers n, m, and k, and then m lines of three integers a_i, b_i, and f_i. It calculates a result for each test case based on the input values and prints the result T times, where T is the number of test cases. The result is calculated using the formula (p * k * k - p * k + 2 * k * C * S) / (2 * C * C) modulo 1000000007, where C is the number of possible pairs of nodes (n * (n - 1) // 2), S is the sum of f_i values, and p is the number of edges. The function reduces the fraction to its simplest form by dividing both numerator and denominator by their greatest common divisor before taking the modulo.

