#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer t, followed by 3 integers n, m, and k, and then m lines, each containing three integers a_i, b_i, and f_i. 1 <= t <= 5 * 10^4, 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2 * 10^5, 1 <= a_i, b_i <= n, a_i != b_i, and 1 <= f_i <= 10^9.
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
        
    #State: The output state is a series of integers, each representing the result of the calculation for a test case. The calculation involves modular arithmetic with a large modulus (10^9 + 7), and the result is the sum of products of the inverse of the number of possible edges in a graph, the number of edges, and the sum of edge weights, all taken modulo the large modulus. The output state will have the same number of integers as the number of test cases in the input.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains an integer t, followed by 3 integers n, m, and k, and then m lines of three integers a_i, b_i, and f_i. It calculates a result for each test case using modular arithmetic with a large modulus (10^9 + 7), involving the inverse of the number of possible edges in a graph, the number of edges, and the sum of edge weights. The function then prints the result of each test case, one per line, as a series of integers representing the calculated sums modulo the large modulus.

