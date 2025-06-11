#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if b <= a:
            print(n * a)
        elif b - a >= n:
            print(int((2 * b - n + 1) * n / 2))
        else:
            print(int((b - a) / 2 * (b - a + 1) + a * n))
        
    #State: The loop will execute 't' times, and for each iteration, it will print the calculated value based on the conditions. The output will be a series of integers, each representing the result of the calculation for the corresponding test case. The value of 't' will be decremented by 1 after each iteration, and the stdin will be empty after the loop finishes executing.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers n, a, and b. It then calculates and prints the result of a mathematical expression based on the values of a and b relative to n. The function handles three cases: when b is less than or equal to a, when b minus a is greater than or equal to n, and when b minus a is less than n. For each test case, it prints the calculated result, and it continues this process until all test cases have been processed, at which point the standard input is empty.

