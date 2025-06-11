#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k (1 <= n <= 100, 0 <= k <= n * (n - 1) / 2).
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k > 1 else 1)
        
    #State: stdin contains zero test cases, `_` is the number of test cases, `n` and `k` are the last test case values, and the output contains the results of all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then prints the result of each test case, which is either n if n-k is greater than 1, or 1 otherwise. The function continues to process test cases until all input has been read, leaving the standard input empty and producing a list of results as output.

