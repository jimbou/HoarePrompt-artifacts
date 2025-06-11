#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer between 1 and 1000, `a`, `b`, and `c` are integers between 0 and 9, `i` is `t-1`, stdin contains 0 lines. If `a` is less than `b` and `b` is less than `c`, 'STAIR' is printed. If `a` is less than `b` and `b` is greater than `c`, 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:The function reads a series of triple-digit numbers from standard input, determines whether each triple forms a "stair" (a < b < c), a "peak" (a < b > c), or neither, and prints the corresponding label ('STAIR', 'PEAK', or 'NONE') for each triple. The function processes a specified number of triples (t) and consumes all input lines, leaving the standard input empty.

