#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is an integer between 1 and 10^4, `i` is `t-1`, `a`, `b`, and `m` are integers between 1 and 10^18 and are the last set of three integers from the input, stdin is empty. If `m` is less than `a` or `m` is less than `b`, the number 2 is printed. Otherwise, the value of the expression `m // a + m // b + 2` is printed, where `m // a` is the integer division of `m` by `a`, `m // b` is the integer division of `m` by `b`, and 2 is an integer constant.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. For each test case, it prints the minimum number of operations required to make a and b greater than or equal to m. If m is less than either a or b, it prints 2. Otherwise, it prints the sum of the integer divisions of m by a and b, plus 2. The function processes all test cases and then terminates, leaving the standard input empty.

