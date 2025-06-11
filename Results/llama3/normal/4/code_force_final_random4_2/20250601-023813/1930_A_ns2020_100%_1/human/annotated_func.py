#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,\ldots,a_{2n} (1 <= a_i <= 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t is 0, stdin is empty, n is an integer between 1 and 50 inclusive, A is a sorted list of 2n integers between 1 and 10^7 inclusive, and the sum of every other element of the list A starting from the first element has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by 2n integers. It sorts the integers in ascending order, calculates the sum of every other integer starting from the first, and prints this sum. The function continues this process until all test cases have been processed, at which point the standard input is empty.

