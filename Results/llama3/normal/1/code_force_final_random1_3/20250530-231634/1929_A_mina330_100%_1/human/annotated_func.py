#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (2 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: ntest is an integer between 0 and 100, itest is equal to ntest, stdin contains no test cases, n is an integer between 2 and 100, a is a sorted list of n integers between 1 and 10^9, and the difference between the last and the first element of the list a is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It sorts the integers in ascending order and prints the difference between the largest and smallest integers for each test case. The function processes all test cases and does not return any value.

