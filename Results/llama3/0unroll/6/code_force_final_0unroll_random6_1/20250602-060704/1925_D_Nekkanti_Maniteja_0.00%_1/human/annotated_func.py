#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t (1 <= t <= 5 * 10^4) on the first line, followed by 3 integers n, m, and k (2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5) on the second line, and m lines of three integers each -- a_i, b_i, f_i (a_i != b_i, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9).
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
        
    #State: The output state after the loop executes all the iterations is a series of integers, each representing the result of the calculation for a test case. The calculation involves modular arithmetic with a large modulus (10^9 + 7), and the result is the sum of products of the inverse of the number of pairs of nodes in a graph, the number of edges, and the sum of edge weights, all taken modulo the large modulus. The output state is a series of these results, one for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, each containing an integer t, followed by 3 integers n, m, and k, and m lines of three integers each. It then performs a calculation involving modular arithmetic with a large modulus (10^9 + 7), using the inverse of the number of pairs of nodes in a graph, the number of edges, and the sum of edge weights. The result is the sum of products of these values, taken modulo the large modulus. The function prints the result for each test case, one per line.

