#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 ≤ n ≤ 2 * 10^5). The second line contains n integers a_1, a_2, …, a_n (-n ≤ a_i ≤ n).
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
        
    #State: t is at least 0, _ is t, n is an integer greater than or equal to 0, a is a list of n integers, p is a list of n integers where the value at index i is mex - a[i], mex is the minimum value between mex and mex - a[i], i is -1, stdin is empty, and the list p is printed for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It then calculates a list of integers p, where each element p[i] is the difference between the minimum value of the list and the corresponding element in the input list a. The function prints the list p for each test case.

