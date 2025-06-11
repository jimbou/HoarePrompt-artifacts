#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: The output state is a list of integers, where each integer is the result of the loop's execution for each test case. The results are calculated based on the values of n and k in each test case, following the conditions specified in the loop body.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two integers n and k. It then calculates and prints the result for each test case based on the values of n and k, following specific conditions. The function outputs a list of integers, where each integer corresponds to the result of the calculation for each test case.

