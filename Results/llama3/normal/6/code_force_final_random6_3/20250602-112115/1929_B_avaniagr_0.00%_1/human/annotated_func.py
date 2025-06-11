#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k, where n is a positive integer greater than or equal to 2 and k is a positive integer greater than or equal to 1 and less than or equal to 4n - 2.
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: The loop has finished executing, `s` is the last line of `stdin`, `n` and `k` are the last pair of integers from the input, `open(0)` is exhausted, and the final value of the expression `(k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k == 4 * n - 2)` is printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case contains two integers n and k. It then calculates and prints a value based on the values of n and k for each test case. The function continues this process until all test cases have been read from standard input, at which point it terminates.

