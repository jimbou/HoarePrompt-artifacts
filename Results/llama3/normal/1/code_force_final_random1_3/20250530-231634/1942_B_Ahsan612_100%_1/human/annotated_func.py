#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-n <= a_i <= n). The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The loop has finished executing, stdin is empty, and the output contains a string of space-separated values for each test case, where each value is mex - ar[i] and mex is equal to the minimum value between the initial value of mex and the minimum value of mex - ar[i] for all i.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints a string of space-separated values for each test case, where each value is the difference between the minimum value (mex) and the corresponding input integer. The mex value is updated to be the minimum of its initial value and the minimum of the differences between mex and each input integer. The function continues this process until all test cases have been processed, at which point the standard input is empty and the output contains the calculated strings for all test cases.

