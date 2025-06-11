#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: The output state will contain `ntest` number of lines, each containing the difference between the maximum and minimum numbers in each test case. The value of `ntest` remains unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains a list of integers. It calculates and prints the difference between the maximum and minimum numbers in each list, without modifying the original input. The function does not return any value, but instead, prints the results directly to the standard output.

