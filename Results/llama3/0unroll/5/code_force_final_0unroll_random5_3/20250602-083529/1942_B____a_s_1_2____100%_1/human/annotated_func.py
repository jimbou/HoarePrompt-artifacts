#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then t times an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
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
        
    #State: The output state will contain t lines, each containing n integers. The integers in each line represent the values of p, which are calculated based on the input values of n and a. The values of p are determined by the formula p[i] = mex - a[i], where mex is the minimum value of p[i] and a[i] is the ith element of the input list a. The values of t and n remain unchanged.

#Overall this is what the function does:This function reads multiple inputs from stdin, where each input consists of an integer t, followed by t sets of inputs, each containing an integer n and n integers a_1 to a_n. It calculates and prints the values of p for each set, where p[i] is determined by the formula p[i] = mex - a[i], and mex is the minimum value of p[i] and a[i]. The function outputs t lines, each containing n integers representing the calculated values of p.

