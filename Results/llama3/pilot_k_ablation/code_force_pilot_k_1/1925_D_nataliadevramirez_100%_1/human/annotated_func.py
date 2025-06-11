#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t, followed by t sets of input. Each set of input contains an integer k, followed by k lines, each containing three integers a_i, b_i, f_i.
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
        
    #State: T is 0, stdin is empty, MOD is 1000000007, n, p, k, S, C, num, den, g, ans are undefined (or more accurately, they are the values from the last iteration of the loop, but since we don't know the input, we can't determine their exact values).

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer t, followed by t sets of input. Each set of input contains an integer k, followed by k lines, each containing three integers a_i, b_i, f_i. It then calculates a value based on the input and prints the result for each test case, modulo 1000000007. The function consumes all input from standard input and leaves it empty.

