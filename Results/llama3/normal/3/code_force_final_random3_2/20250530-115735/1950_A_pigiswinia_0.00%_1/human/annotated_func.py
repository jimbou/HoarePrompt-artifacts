#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer between 1 and 1000, `i` is `t-1`, `a`, `b`, and `c` are integers assigned from the input, stdin contains at least `t-1` lines. If `a` is less than `b` and `b` is less than `c`, then 'STAIRS' is printed. If `a` is less than `b` and `b` is greater than `c`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of triple-digit numbers from standard input, determines the relationship between the digits, and prints a classification ('STAIRS', 'PEAK', or 'NONE') based on whether the digits form an increasing sequence, a peak, or neither.

