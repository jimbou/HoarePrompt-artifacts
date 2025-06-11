#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        kq = 0
        
        for i in range(0, len(a) // 2, 1):
            kq = kq + a[len(a) - i - 1] - a[i]
        
        print(kq)
        
    #State: ntest is an integer between 1 and 500 inclusive, itest is ntest, n is an integer between 2 and 100 inclusive, a is a sorted list of n integers that must have at least 2 elements, kq is the sum of the differences between the elements at the corresponding indices from the end and the start of the list a, stdin contains 0 test cases, i is len(a) // 2 - 1, and the sum of the differences between the elements at the corresponding indices from the end and the start of the list a, which is kq, is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts the integers in ascending order, calculates the sum of the differences between the elements at the corresponding indices from the end and the start of the list, and prints this sum for each test case. The function processes all test cases provided in the input and does not return any value.

