#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two integers n and k such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output state after the loop executes all the iterations will be a series of integers, each representing the result of the calculation for a given test case. The integers will be either 1, the ceiling of k/2, or k/2 + 1, depending on the values of n and k in each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two integers n and k. It then calculates and prints the result for each test case, which is either 1, the ceiling of k/2, or k/2 + 1, depending on the values of n and k. The function processes all test cases and outputs the corresponding results.

