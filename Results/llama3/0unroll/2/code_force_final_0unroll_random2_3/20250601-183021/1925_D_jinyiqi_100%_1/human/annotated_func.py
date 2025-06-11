#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains 3 integers n, m, and k, followed by m lines, each containing three integers a_i, b_i, and f_i. 2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2*10^5, 1 <= a_i, b_i <= n, a_i != b_i, and 1 <= f_i <= 10^9.
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
        
    #State: The loop has executed t-1 times, and the values of the variables in the loop head and body have been updated accordingly. The variable t is now 1, and the variables n, m, k, sum_f, a, b, f, cn2, p, q, and gcd have been updated with the values from the last test case. The output of the loop, which is the result of the modular inverse calculation, has been printed to the console for each test case. The state of the other variables, M and stdin, remains unchanged.

#Overall this is what the function does:Calculates and prints the modular inverse of a calculated value for each test case in the input, where the value is derived from the number of nodes, edges, and a given constant, and the modular inverse is calculated using the pow function with a modulus of 10^9 + 7.

