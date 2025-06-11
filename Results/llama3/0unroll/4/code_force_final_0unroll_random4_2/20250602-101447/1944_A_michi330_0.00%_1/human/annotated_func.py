#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 1 <= n <= 100 and 0 <= k <= n * (n - 1) / 2.
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The loop has executed all the iterations, and the output state is a series of printed values, either 1 or n-1, depending on the value of k in each test case. The value of t remains unchanged, and the stdin is empty after reading all the test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two integers n and k. It then prints the value 1 if k is greater than or equal to n-1, and n-1 otherwise, for each test case. The function does not return any value but instead prints the results directly to the console, leaving the standard input empty after processing all test cases.

