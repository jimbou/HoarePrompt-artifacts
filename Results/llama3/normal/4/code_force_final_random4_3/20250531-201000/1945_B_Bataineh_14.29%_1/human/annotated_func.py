#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is an integer between 0 and 10^4 (inclusive), `i` is `t`, `a`, `b`, `m` are integers (1 <= a, b, m <= 10^18), stdin is empty. If `m` is less than `a` or `m` is less than `b`, the number 2 is printed. Otherwise, the value of the expression `m // a + m // b + 2` is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. For each case, it calculates and prints the minimum number of operations required to make a and b equal to m, which is either 2 if m is less than a or b, or the sum of m divided by a, m divided by b, and 2 otherwise. The function processes all test cases and then terminates, leaving the standard input empty.

