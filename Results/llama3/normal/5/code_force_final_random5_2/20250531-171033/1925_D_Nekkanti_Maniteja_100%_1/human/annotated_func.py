#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains multiple lines. The first line contains three integers n, m, and k. The next m lines contain three integers each.
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
        
    #State: The loop has finished executing, and the final output state is the sum of all the output states after each iteration, modulo M.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of multiple lines. For each test case, it reads three integers (n, m, k) and then m lines of three integers each. It calculates a value 's' based on these inputs and prints the result modulo M (10^9 + 7). The function repeats this process for all test cases and outputs the sum of all results modulo M.

