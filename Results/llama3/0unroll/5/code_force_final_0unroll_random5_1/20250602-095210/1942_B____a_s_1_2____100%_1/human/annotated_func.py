#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (-n <= a_i <= n).
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
        
    #State: The output state is a list of t lines, where each line contains n integers. The integers in each line are the values of p, which are calculated based on the input values of n and a. The values of p are determined by the formula p[i] = mex - a[i], where mex is the minimum value of p[i] and n. The output state is a transformed version of the input state, where each test case is processed and the corresponding values of p are printed.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the transformed output for each test case. It accepts a series of integers as input, where the first integer t represents the number of test cases, followed by t test cases. Each test case consists of an integer n, representing the number of elements in the test case, followed by n integers. The function calculates a new set of integers p based on the input values and prints the transformed output for each test case. The output is a list of t lines, where each line contains n integers representing the calculated values of p.

