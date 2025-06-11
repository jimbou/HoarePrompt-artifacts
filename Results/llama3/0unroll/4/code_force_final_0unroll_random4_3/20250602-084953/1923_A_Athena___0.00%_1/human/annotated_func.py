#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains one integer n (2 <= n <= 50). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1). At least one a_i is 1.
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
        
    #State: Output State: `t` is a positive integer, stdin contains t-1 test cases. Each test case contains two lines. The first line contains one integer n (2 <= n <= 50). The second line contains n integers a_1, a_2, ..., a_n (0 <= a_i <= 1). At least one a_i is 1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers (0s and 1s). It then processes each test case by removing leading and trailing zeros from the list, prints the modified list, and finally prints the count of zeros in the modified list. The function repeats this process for all test cases provided in the input.

