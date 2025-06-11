#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-n <= a_i <= n). The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The output state will be a list of integers, where each integer is the result of subtracting the corresponding element in the input list from the minimum excluded value (mex) of the input list. The mex value is updated in each iteration to be the minimum of the current mex and the difference between the current mex and the current element in the input list. The output list is in reverse order of the input list.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It calculates the minimum excluded value (mex) of the input list and updates it iteratively. For each element in the input list, it subtracts the element from the current mex and updates the mex if necessary. The function then prints the resulting list of integers in reverse order of the input list. The output list represents the difference between the mex and each corresponding element in the input list, with the mex updated at each step.

