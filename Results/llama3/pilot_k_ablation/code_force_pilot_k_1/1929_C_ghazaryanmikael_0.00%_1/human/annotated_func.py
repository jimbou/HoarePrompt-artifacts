#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers: k, x, and a, where k is an integer between 2 and 30, x is an integer between 1 and 100, and a is an integer between 1 and 10^9.
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 0
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('YES' if a >= s else 'NO')
        
    #State: stdin is empty, `k`, `x`, and `a` are the last integers read from stdin, `s` is 0, `_` is the number of test cases, 'YES' or 'NO' is printed for each test case

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers: k, x, and a. It calculates a value s based on k and x, and then prints 'YES' if a is greater than or equal to s, and 'NO' otherwise. The function processes all test cases and leaves the standard input empty after execution.

