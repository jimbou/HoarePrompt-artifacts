#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: The output will consist of multiple lines of output for each iteration of the outer loop (t times). Each set of output for an iteration will start with a line containing a sum value and a number (n + r), followed by multiple lines of numbers. The exact numbers and their arrangement depend on the values of n provided in the input. The state of variables not affected by the loop (e.g., t after the loop finishes) remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing a single integer n representing the size of a matrix. For each test case, it calculates a sum value and a number (n + r), where r is determined based on the condition n * (n + 1) // 2 > i * n. It then prints the sum value and (n + r) followed by multiple lines of numbers arranged in a specific pattern. The function repeats this process for each test case, producing multiple sets of output.

