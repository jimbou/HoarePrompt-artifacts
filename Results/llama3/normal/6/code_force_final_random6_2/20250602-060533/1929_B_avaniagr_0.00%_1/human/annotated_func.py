#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k (2 <= n <= 10^8, 1 <= k <= 4n - 2).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: The loop has executed for all test cases in stdin, and the output state is the sum of the values of the expression `(k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k == 4 * n - 2)` for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints the sum of the values of a specific expression for each test case, which depends on the values of n and k. The function processes all test cases and outputs the calculated sums.

