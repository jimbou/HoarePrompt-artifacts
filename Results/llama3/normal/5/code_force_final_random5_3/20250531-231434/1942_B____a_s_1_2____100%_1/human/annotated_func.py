#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
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
        
    #State: t is 0, stdin contains 0 test cases, _ is t, n is an integer between 1 and 2 * 10^5 (inclusive), a is a list of n integers, p is a list of n values where all values are mex - a[i] for i from 0 to n-1, mex is equal to the minimum value between mex and mex - a[0], and i is -1, and the list p is printed

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates a list of values p, where each value is the difference between the minimum value of the list and the corresponding value in the input list a. The function prints the list p for each test case. The function accepts no parameters and returns no value, but it modifies the standard input by consuming the test cases. The final state of the program is that the standard input is empty, and the list p has been printed for each test case.

