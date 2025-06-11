#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is an integer between 1 and 10^4, `i` is `t-1`, `a` is an integer between 1 and 10^18, `b` is an integer between 1 and 10^18, `m` is an integer between 1 and 10^18, stdin contains 0 lines. If `m` is less than `a` or `m` is less than `b`, the number 2 is printed. Otherwise, if `m` is larger than or equal to `a` and `m` is larger than or equal to `b`, the result of `m // a + m // b + 2` is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. It then calculates and prints the minimum number of operations required to make a and b equal to m. If m is less than either a or b, it prints 2. Otherwise, it prints the result of m divided by a, plus m divided by b, plus 2. The function processes all test cases and then terminates, leaving the standard input empty.

