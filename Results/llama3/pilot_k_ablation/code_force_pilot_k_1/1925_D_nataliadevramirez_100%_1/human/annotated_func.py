#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains 3 integers n, m, and k, followed by m lines, each containing three integers a_i, b_i, and f_i. n is the number of children, m is the number of pairs of friends, and k is the number of excursions. a_i and b_i are the indices of the pair of children who are friends, and f_i is their friendship value. 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2*10^5, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9, and a_i != b_i.
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
        
    #State: T is 0, stdin is empty, n, p, k, S, i, C, num, den, ans are undefined (or have arbitrary values), and nothing is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing the number of children, pairs of friends, and excursions. It calculates the probability of a child going on an excursion with a friend, given the friendship values and the number of excursions. The function then prints the result for each test case, modulo 1,000,000,007. After processing all test cases, the function leaves the input stream empty and does not retain any information from the input.

