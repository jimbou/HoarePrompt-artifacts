#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t (1 <= t <= 5 * 10^4) on the first line, followed by 3 integers n, m, and k (2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5) on the second line, and then m lines containing three integers each -- a_i, b_i, f_i (a_i != b_i, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9).
    for i in range(int(input())):
        n, m, k = map(int, input().split())
        
        M = 10 ** 9 + 7
        
        c = pow(n * (n - 1) // 2, -1, M)
        
        s = 0
        
        a = 0
        
        for i in range(m):
            u, v, f = map(int, input().split())
            a += f
        
        for i in range(k):
            s = s + c * i * c * m + c * a
        
        print(s % M)
        
    #State: The final state of the program after executing all iterations of the loop will be the sum of the products of the modular inverses of the number of pairs of nodes, the number of edges, and the sum of the frequencies of the edges, all taken modulo 10^9 + 7. The output will be a single integer value for each test case, representing the final state of the program after executing all iterations of the loop.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains an integer t, followed by 3 integers n, m, and k, and then m lines of three integers each. It calculates the sum of the products of the modular inverses of the number of pairs of nodes, the number of edges, and the sum of the frequencies of the edges, all taken modulo 10^9 + 7, and prints the result for each test case. The function effectively computes a weighted sum of the modular inverses of the number of pairs of nodes, the number of edges, and the sum of the frequencies of the edges, and outputs the final state of the program after executing all iterations of the loop.

