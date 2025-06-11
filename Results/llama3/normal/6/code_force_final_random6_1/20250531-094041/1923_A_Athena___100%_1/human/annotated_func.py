#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines: the first line contains one integer n (2 <= n <= 50), and the second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. In each test case, at least one cell contains a chip.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        res = 0
        
        while a and a[0] == 0:
            a.pop(0)
        
        while a and a[-1] == 0:
            a.pop()
        
        for i in range(len(a)):
            if a[i] == 0:
                res += 1
        
        print(res)
        
    #State: `a` is an empty list, `t` is 0, `n` is an integer, `res` is the number of zeros in the last list `a`, `i` is the last index of the last list `a`, `_` is equal to the initial value of `t`, and `stdin` is empty.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the number of zeros in each test case after removing leading and trailing zeros. It takes no arguments and returns no value, only printing the results to the console. The function modifies the input list by removing leading and trailing zeros and counts the remaining zeros. After execution, the input list is empty, and the input stream is exhausted.

