#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains the number of test cases t (1 <= t <= 500). Each test case contains a single integer n (1 <= n <= 500) — the size of the matrix a.
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
        
    #State: t is 0, _ is t, i is n, j is n + r, stdin contains no test cases, r is n, sum is either n * (n + 1) * (n + 2) // 6 or n * (n + 1) // 2, and n is at least 1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a single integer n representing the size of a matrix. It calculates a sum based on the value of n and prints the sum along with the value of n plus an additional calculated value r. The function then prints a series of lines representing a matrix, where the first n lines have a specific pattern and the remaining lines have a different pattern. The function repeats this process for each test case and consumes all input from standard input, leaving no test cases remaining.

