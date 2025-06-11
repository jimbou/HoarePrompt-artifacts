#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t (1 <= t <= 5 * 10^4) followed by 3 integers n, m, and k (2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2 * 10^5), then m lines, each containing three integers a_i, b_i, and f_i (a_i != b_i, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9).
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 1, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: The output state is the sum of the products of the modular inverses of the number of nodes, the number of edges, and the number of operations, modulo 10^9 + 7, for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer t, followed by three integers n, m, and k, and then m lines of three integers each. It calculates the sum of the products of the modular inverses of the number of nodes, the number of edges, and the number of operations, modulo 10^9 + 7, for each test case, and prints the result. The function does not modify the input variables and only uses them to compute the output. The final state of the program is the output of the calculated sums for each test case.

