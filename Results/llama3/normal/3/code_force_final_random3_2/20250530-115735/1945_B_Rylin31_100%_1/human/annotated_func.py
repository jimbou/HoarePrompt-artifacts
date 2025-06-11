#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: `t` is an integer between 1 and 10^4, `i` is `t-1`, `a`, `b`, `m` are integers, stdin contains 0 lines, and `m // a + m // b + 2` has been printed `t` times.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of three integers a, b, and m, and prints the result of the expression m // a + m // b + 2 for each test case.

