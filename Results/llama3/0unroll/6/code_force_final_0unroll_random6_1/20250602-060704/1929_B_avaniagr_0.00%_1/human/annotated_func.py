#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: an integer n (2 <= n <= 10^8) and an integer k (1 <= k <= 4n - 2).
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: The output state will be a series of integers, each representing the result of the calculation for a given test case. The calculation is based on the values of n and k, and the output will be the sum of the products of k // 2 + k % 2 and a boolean value indicating whether k is less than 4 * n - 3, plus the product of 2 * n and a boolean value indicating whether k is greater than or equal to 4 * n - 3, plus a boolean value indicating whether k is equal to 4 * n - 2.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of two integers, n and k. It calculates a result for each test case based on the values of n and k, and prints the results. The calculation involves determining the sum of the products of k // 2 + k % 2 and a boolean value indicating whether k is less than 4 * n - 3, plus the product of 2 * n and a boolean value indicating whether k is greater than or equal to 4 * n - 3, plus a boolean value indicating whether k is equal to 4 * n - 2. The function outputs a series of integers, each representing the result of the calculation for a given test case.

