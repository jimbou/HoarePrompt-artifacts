#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t, a positive integer. Each test case contains two positive integers n and m.
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: t is a positive integer greater than or equal to 0, T is equal to t, stdin contains no test cases, n is an integer, m is an integer, ans is equal to n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1)), b is equal to min(n, m) + 1, and the value of ans which is n + sum((n + b) // (b * b) for b in range(2, min(n, m) + 1)) is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two positive integers n and m. It calculates a value 'ans' for each test case, which is initially set to n, and then iteratively adds the result of the expression (n + b) // (b * b) for b ranging from 2 to the minimum of n and m. Finally, it prints the calculated 'ans' value for each test case.

