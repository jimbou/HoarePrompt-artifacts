#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n, an integer m, an integer k, and m lines of input, each containing three integers a, b, and f. The input is well-formed and valid according to the problem description.
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
        
    #State: The output state will be the sum of the products of the modular multiplicative inverse of the number of pairs of nodes in the graph, the number of edges, and the sum of the frequencies of the edges, taken modulo 10^9 + 7, for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n, an integer m, an integer k, and m lines of input containing three integers a, b, and f. It calculates the sum of the products of the modular multiplicative inverse of the number of pairs of nodes in the graph, the number of edges, and the sum of the frequencies of the edges, taken modulo 10^9 + 7, for each test case, and prints the result.

