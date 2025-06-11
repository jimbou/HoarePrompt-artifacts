#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is an integer (1 <= t <= 10^4) and `t` is greater than or equal to 0, `i` is `t`, `a`, `b`, `m` are integers (1 <= a, b, m <= 10^18), stdin contains 0 lines. If `m` is less than both `a` and `b`, then the number 2 is printed. Otherwise, if `m` is less than `a` and greater than `b`, then 2 plus the integer division of `m` by `b` is printed. If `m` is greater than `a` and less than `b`, then 2 plus the integer division of `m` by `a` is printed. Otherwise, if `m` is either less than or equal to `a` or `m` is larger or equal to `b`, then the integer division of `m` by `a` plus the integer division of `m` by `b` plus 2 is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. It then calculates and prints the minimum number of operations required to make a and b greater than or equal to m, considering the cases where m is less than both a and b, less than a but greater than b, less than b but greater than a, or greater than or equal to either a or b. The function processes all test cases and prints the results accordingly.

