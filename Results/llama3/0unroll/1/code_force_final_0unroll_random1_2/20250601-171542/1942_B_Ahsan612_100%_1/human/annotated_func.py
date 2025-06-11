#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-n ≤ a_i ≤ n).
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
        
    #State: The output state contains multiple test cases. Each test case contains a list of integers, where each integer is the difference between the minimum excluded value (mex) and the corresponding integer in the input list, and the mex is updated to be the minimum of the current mex and the difference.

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It calculates the difference between the minimum excluded value (mex) and each integer in the list, updating the mex to be the minimum of the current mex and the difference. The function then prints the resulting list of differences for each test case.

