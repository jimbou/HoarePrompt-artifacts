#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 50). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. In each test case, at least one cell contains a chip.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        print(a)
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: `t` is an integer larger than 0, `_` is equal to `t-1`, `n` is an integer, `a` is an empty list, `res` is equal to 0, `i` is equal to 0, `stdin` is empty, and the value of `res` is printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the number of free cells (containing 0) in each test case. It takes no parameters and returns no value, but instead prints the results directly. The function iterates over multiple test cases, each containing a list of cells with chips (1) or free cells (0). It trims leading and trailing free cells from the list, then counts and prints the number of remaining free cells.

