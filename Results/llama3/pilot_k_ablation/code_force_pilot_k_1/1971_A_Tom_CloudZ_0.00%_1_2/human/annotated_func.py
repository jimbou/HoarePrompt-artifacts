#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: `t` is an integer between 1 and 100 inclusive, `a` is an integer between 0 and 9 inclusive, `b` is an integer between 0 and 9 inclusive, `_` is `t-1`, stdin is empty, and the maximum and minimum of each pair of `x` and `y` from the original `t` lines are printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the first integer specifies the number of pairs to read, and each pair consists of two integers between 0 and 9. It then prints the maximum and minimum of each pair, in that order, for all pairs read. The function does not return any value, and its primary effect is to produce output based on the input pairs.

