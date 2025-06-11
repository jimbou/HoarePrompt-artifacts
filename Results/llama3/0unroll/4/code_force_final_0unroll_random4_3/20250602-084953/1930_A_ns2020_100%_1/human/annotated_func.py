#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 5000) followed by t test cases. Each test case contains an integer n (1 <= n <= 50) followed by 2n integers a_1,a_2,\ldots,a_{2n} (1 <= a_i <= 10^7).
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: The sum of the smallest n numbers in each test case is printed, and t is 0.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case contains an integer n followed by 2n integers. For each test case, it sorts the 2n integers, calculates the sum of the smallest n numbers, and prints the result. The function continues this process until all test cases have been processed, at which point it terminates.

