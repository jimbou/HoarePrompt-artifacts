#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (2 <= n <= 50) followed by a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_i <= 1) where a_i = 0 means the i-th cell is free and a_i = 1 means the i-th cell contains a chip. In each test case, at least one cell contains a chip.
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
        
    #State: The number of zeros in the middle of each test case list (i.e., excluding leading and trailing zeros) will be printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of binary digits (0s and 1s) representing free cells and cells containing chips, respectively. It then processes each test case by removing leading and trailing zeros, counts the number of zeros in the remaining list (i.e., the zeros in the middle), and prints this count for each test case.

