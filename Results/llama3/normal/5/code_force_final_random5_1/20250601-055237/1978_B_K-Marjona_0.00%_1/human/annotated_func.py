#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers n, a, and b (1 <= n, a, b <= 10^9).
    for _ in range(int(input())):
        n, a, b = map(int, input().split())
        
        k = min(n, b - a)
        
        if b <= a:
            print(a * n)
        else:
            print((b + (b - k + 1)) // 2 * k + (n - k) * a)
        
    #State: All test cases have been processed, and the output for each test case has been printed. The loop has executed for a number of times equal to the number of test cases in the input.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing three integers n, a, and b. For each test case, it calculates and prints the minimum cost based on the values of n, a, and b. If b is less than or equal to a, the cost is simply a times n. Otherwise, the cost is calculated using the formula (b + (b - k + 1)) // 2 * k + (n - k) * a, where k is the minimum of n and b - a. The function continues processing test cases until all input has been read, printing the result for each case.

