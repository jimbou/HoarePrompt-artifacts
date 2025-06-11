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
        
    #State: The output state is a list of integers, where each integer is the result of subtracting the corresponding input integer from the maximum possible value (n) minus the current minimum value (mex). The list is in reverse order of the input list.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates and prints a list of integers, where each integer is the result of subtracting the corresponding input integer from the maximum possible value (n) minus the current minimum value (mex), in reverse order of the input list. The function processes multiple test cases and outputs the results for each case.

