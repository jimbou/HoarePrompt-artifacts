#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        p = [-1] * n
        
        mex = n
        
        for i in range(n - 1, -1, -1):
            p[i] = mex - a[i]
            mex = min(mex, p[i])
        
        print(*p)
        
    #State: t is at least 1, _ is t - 1, n is an integer between 1 and 2 * 10^5, a is a list of n integers, p is a list of n values where the value at index i is mex - a[i], mex is the minimum of its original value and all mex - a[i], i is -1, stdin contains 0 test cases, and the list of values p is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then calculates a new list of values p, where each value at index i is the minimum of the original value and the difference between the current minimum and the corresponding value in the input list. Finally, it prints the list of values p for each test case.

