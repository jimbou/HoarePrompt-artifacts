#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (2 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: Output State: The output state will contain the difference between the maximum and minimum values of each test case, printed on separate lines. The value of `ntest` remains unchanged, and `stdin` is empty after all test cases have been processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It calculates and prints the difference between the maximum and minimum values of each test case, without modifying the original input values or the number of test cases. The function processes all test cases and leaves the standard input empty.

