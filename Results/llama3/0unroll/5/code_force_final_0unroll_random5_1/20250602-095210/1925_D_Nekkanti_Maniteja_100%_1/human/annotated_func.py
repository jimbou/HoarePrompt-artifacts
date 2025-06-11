#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer n, m, and k on the first line, and m lines of three integers each on the following lines. 2 <= n <= 10^5, 0 <= m <= min(10^5, n*(n-1)/2), 1 <= k <= 2*10^5.
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
        
    #State: The output state after the loop executes all the iterations is a series of integers, each representing the result of the calculation for a test case. The calculation involves modular arithmetic with a large modulus (M = 10^9 + 7) and uses the inverse of the number of possible pairs of nodes in a graph (c = pow(n * (n - 1) // 2, -1, M)). The result for each test case is the sum of the products of the inverse of the number of pairs, the number of pairs, the frequency of each pair, and the inverse of the number of pairs again, all taken modulo M. The output state is a series of these results, one for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n, m, and k, followed by m lines of three integers each. It then performs a series of calculations involving modular arithmetic with a large modulus (10^9 + 7) and the inverse of the number of possible pairs of nodes in a graph. The result for each test case is the sum of the products of the inverse of the number of pairs, the number of pairs, the frequency of each pair, and the inverse of the number of pairs again, all taken modulo M. The function prints the result for each test case, one per line.

