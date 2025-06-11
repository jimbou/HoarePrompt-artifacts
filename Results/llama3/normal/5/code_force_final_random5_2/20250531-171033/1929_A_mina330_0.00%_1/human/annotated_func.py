#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains a single integer n (2 <= n <= 100). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: itest is equal to ntest, ntest is an integer between 0 and 100 (inclusive), stdin contains no test cases, n is an integer, a is a sorted list of integers, kq is the sum of the differences between the corresponding elements from the end and the beginning of a, i is 0, and the sum of the differences between the corresponding elements from the end and the beginning of a which is kq is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It sorts the integers in ascending order, calculates the sum of the differences between corresponding elements from the end and the beginning of the sorted list, and prints this sum for each test case. The function processes all test cases and does not return any value.

