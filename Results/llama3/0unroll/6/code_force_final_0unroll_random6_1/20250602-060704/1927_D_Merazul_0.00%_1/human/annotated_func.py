#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains a line with an integer n, a line with n space-separated integers, a line with an integer q, and q lines with two space-separated integers each. All integers are non-negative and within the given constraints.
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        *_, k = R()
        
        a = {*R()}
        
        b = {*R()}
        
        f = 1
        
        m = n = k // 2
        
        for i in range(1, k + 1):
            u = i in a
            v = i in b
            f &= u | v
            m -= u & ~v
            n -= ~u & v
        
        print('YNEOS'[f ^ 1 or m | n < 0::2])
        
    #State: The output state after the loop executes all the iterations is that the variable 't' is 0, and the standard output contains a series of strings, each of which is either 'Y', 'N', 'E', 'O', or 'S', depending on the values of 'f', 'm', and 'n' in each iteration. The values of other variables in the initial state remain unchanged.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n, a line of n space-separated integers, an integer q, and q lines of two space-separated integers. It then checks for each test case if a certain condition is met, based on the presence of integers in two sets, and prints a string ('Y', 'N', 'E', 'O', or 'S') to standard output indicating the result. The function continues this process until all test cases have been processed, leaving the standard output containing a series of result strings and the variable 't' set to 0.

