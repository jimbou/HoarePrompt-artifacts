#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains 3 integers n, m, and k, followed by m lines, each containing three integers a_i, b_i, and f_i. 1 <= t <= 5 * 10^4, 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5, 1 <= a_i, b_i <= n, a_i != b_i, and 1 <= f_i <= 10^9.
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
        
    #State: Output State: The loop has executed T times, and for each iteration, it has calculated and printed the value of 'ans' which is the result of the expression (num * den) % MOD, where num and den are calculated based on the input values n, p, k, and S. The values of T, MOD, and the input values for each test case remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers n, m, and k, followed by m lines of three integers a_i, b_i, and f_i. It calculates a value 'ans' for each test case based on the input values and prints the result. The function iterates through all test cases, performing calculations and printing results without modifying the input values or any external state.

