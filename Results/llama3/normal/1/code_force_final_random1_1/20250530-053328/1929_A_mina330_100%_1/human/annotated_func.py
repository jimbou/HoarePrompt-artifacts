#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 500) followed by t test cases. Each test case consists of an integer n (2 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: ntest is 0, itest is equal to the initial value of ntest, stdin contains 0 test cases, n is an integer between 2 and 100 (inclusive), a is a sorted list of n integers between 1 and 10^9 (inclusive), and the difference between the last and first element of the list a which is a[len(a) - 1] - a[0] is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts the integers in ascending order and prints the difference between the largest and smallest integer in each test case. The function continues this process until all test cases have been processed, at which point it terminates.

