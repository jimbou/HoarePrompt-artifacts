#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        res = [None] * n
        
        mex = n
        
        for i in range(len(ar) - 1, -1, -1):
            res[i] = mex - ar[i]
            if mex > mex - ar[i]:
                mex = mex - ar[i]
        
        print(' '.join(str(x) for x in res))
        
    #State: _ is t-1, n is an integer, ar is a list of n integers, res is a list of n values where res[i] is mex - ar[i], mex is the minimum value between the current value of mex and mex - ar[i] for all i in range(len(ar) - 1, -1, -1), i is -1, stdin contains 0 test cases, and this is printed: a string of space-separated integers representing the values in the res list

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the results. It accepts a series of test cases, where each test case consists of an integer n followed by a list of n integers. The function calculates a new list of values, where each value is the difference between the minimum value (mex) and the corresponding value in the input list. The function then prints the resulting list of values as a string of space-separated integers. The function repeats this process for each test case until all test cases have been processed, at which point stdin is empty.

