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
        
    #State: The loop will execute t times, each time taking an integer n as input and printing the sum of the first n natural numbers and the value of n plus the largest integer r such that n*(n+1)//2 > i*n. The loop will also print a series of lines, each containing either 1 or 2, followed by a number from 1 to n, and then the numbers from 1 to n. The value of t will be decremented by 1 after each iteration, and the final output state will have t equal to 0.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains a single integer n representing the size of a matrix. For each test case, it calculates the sum of the first n natural numbers and the value of n plus the largest integer r such that n*(n+1)//2 > i*n. It then prints the calculated sum and the value of n plus r, followed by a series of lines containing either 1 or 2, a number from 1 to n, and the numbers from 1 to n. The function repeats this process for each test case, with the number of test cases determined by the initial input.

