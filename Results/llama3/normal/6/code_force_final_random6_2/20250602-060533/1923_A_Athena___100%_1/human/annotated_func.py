#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines: the first line contains an integer n (2 <= n <= 50), and the second line contains n space-separated integers a_1, a_2, ..., a_n (0 <= a_i <= 1). In each test case, at least one cell contains a chip (a_i = 1).
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
        
    #State: t is 0, n is an integer, a is a list of integers with no leading zeros and no trailing zeros, res is the number of zeros in a, i is len(a), stdin contains no test cases, and the number of zeros in the list a which is res is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of binary digits (0s and 1s). It processes each test case by removing leading and trailing zeros from the list, then counts the number of zeros remaining in the list. The function prints the count of zeros for each test case.

