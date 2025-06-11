#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains 3 integers n, m and k, followed by m lines, each containing three integers a_i, b_i, f_i. n is an integer between 2 and 10^5, m is an integer between 0 and min(10^5, n*(n-1)/2), k is an integer between 1 and 2*10^5, a_i and b_i are integers between 1 and n, and f_i is an integer between 1 and 10^9.
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
        
    #State: n is an integer, m is an integer and must be greater than or equal to 0, k is an integer and must be greater than or equal to 0, M is 10^9 + 7, c is the modular multiplicative inverse of n * (n - 1) // 2 modulo M, s is k * (k - 1) // 2 * c * m + k * c * a, a is the sum of all f values, i is k - 1, u is an integer, v is an integer, stdin contains no more test cases, and the value of s modulo M is being printed, where s is k * (k - 1) // 2 * c * m + k * c * a and M is 10^9 + 7

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three integers n, m, and k, followed by m lines of three integers a_i, b_i, and f_i. It calculates the modular multiplicative inverse of n * (n - 1) // 2 modulo 10^9 + 7, sums up all f_i values, and then computes a value s based on the formula k * (k - 1) // 2 * c * m + k * c * a, where c is the modular multiplicative inverse and a is the sum of f_i values. Finally, it prints the value of s modulo 10^9 + 7 for each test case.

