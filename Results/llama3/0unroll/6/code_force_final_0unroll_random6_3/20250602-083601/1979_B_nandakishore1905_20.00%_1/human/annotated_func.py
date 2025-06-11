#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two distinct non-negative integers x and y.
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: The output state will contain the results of the loop's execution for each test case. For each test case, the output will be the result of the calculations performed inside the loop, which depends on the values of n and m. Specifically, the output will be either the absolute difference between n and m (k), 1, 2, or k minus 2 to the power of (p-1), where p is the length of the binary representation of k. The output state will contain these results for each test case, in the same order as the input test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains two distinct non-negative integers. It calculates and prints the result for each test case based on the absolute difference between the two integers. The result is either the absolute difference itself, 1, 2, or the absolute difference minus 2 to the power of the second-to-last bit position in the binary representation of the absolute difference. The function outputs the results for all test cases in the same order as the input.

