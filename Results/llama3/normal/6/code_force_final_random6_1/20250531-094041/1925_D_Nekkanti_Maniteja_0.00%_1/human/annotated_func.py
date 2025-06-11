#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains an integer k, then k lines, each containing three integers n, m, and k (2 <= n <= 10^5, 0 <= m <= min(10^5, n(n-1)/2), 1 <= k <= 2 * 10^5), followed by m lines, each containing three integers a_i, b_i, and f_i (a_i != b_i, 1 <= a_i, b_i <= n, 1 <= f_i <= 10^9).
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
        
    #State: n is an integer, m is an integer greater than or equal to 0, k is 0, M is 1000000007, c is the modular multiplicative inverse of n*(n-1) modulo M, s is k * c * a + c * m * (k * (k-1) / 2), a is the sum of all f values, u is an integer, v is an integer, f is an integer, i is k, stdin is empty, and the remainder of s divided by M is being printed.

#Overall this is what the function does:Functionality: This function reads multiple test cases from standard input, each containing an integer k, followed by k lines of three integers (n, m, k), and then m lines of three integers (a_i, b_i, f_i). It calculates the sum of all f_i values and uses this sum, along with the values of n, m, and k, to compute a result s. The function then prints the remainder of s divided by a large modulus M (1000000007) for each test case.

