#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 100) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        year = 0
        
        for ai in a:
            year += year % ai or ai
        
        print(year)
        
    #State: `t` is 0, `n` is an integer, `a` is an empty list, `ai` is not defined, `year` is the least common multiple of all elements in the original list `a`, `_` is `t`, `stdin` contains 0 test cases, and the least common multiple of all elements in the original list `a` which is `year` is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It calculates the least common multiple (LCM) of the integers in each test case and prints the LCM. The function processes all test cases and does not return any value, only printing the LCM for each test case.

