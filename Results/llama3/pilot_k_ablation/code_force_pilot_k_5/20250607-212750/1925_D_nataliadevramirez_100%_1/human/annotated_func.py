#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t (1 <= t <= 5 * 10^4) on the first line, followed by 3 integers n, m, and k (2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5) on the second line, and then m lines, each containing three integers a_i, b_i, and f_i (1 <= a_i, b_i <= n, 1 <= f_i <= 10^9).
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
        
    #State: T is an integer between 1 and 5 * 10^4, MOD is 1000000007, T is greater than or equal to 0, _ is T, n is an integer, k is an integer, S is the sum of the third element of all lines of the input, p is an integer and greater than or equal to 0, i is p, C is n * (n - 1) // 2, num is (p * k * k - p * k + 2 * k * C * S) // math.gcd(p * k * k - p * k + 2 * k * C * S, 2 * C * C), den is pow(2 * C * C // math.gcd(p * k * k - p * k + 2 * k * C * S, 2 * C * C), -1, MOD), ans is ((p * k * k - p * k + 2 * k * C * S) // math.gcd(p * k * k - p * k + 2 * k * C * S, 2 * C * C)) * pow(2 * C * C // math.gcd(p * k * k - p * k + 2 * k * C * S, 2 * C * C), -1, MOD) % MOD, stdin contains multiple test cases with p less lines than before, and the answer to the problem which is ((p * k * k - p * k + 2 * k * C * S) // math.gcd(p * k * k - p * k + 2 * k * C * S, 2 * C * C)) * pow(2 * C * C // math.gcd(p * k * k - p * k + 2 * k * C * S, 2 * C * C), -1, MOD) % MOD is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer t, followed by three integers n, m, and k, and then m lines containing three integers a_i, b_i, and f_i. It calculates a value based on these inputs using modular arithmetic and prints the result. The function processes all test cases and prints the corresponding results.

