#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
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
        
    #State: n is an integer greater than 0, ar is a list of n integers, res is a list of n values where res[i] is mex - ar[i] for all i, mex is the minimum value in res, _ is t-1, stdin contains 0 test cases, i is -1, and the list res is printed, where each element of res is the difference between the minimum value in res (mex) and the corresponding element in ar

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the results. It accepts an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n). The function calculates the minimum value (mex) in the result list and prints the list of differences between mex and each corresponding element in the input list. The function processes all test cases and prints the results for each case.

