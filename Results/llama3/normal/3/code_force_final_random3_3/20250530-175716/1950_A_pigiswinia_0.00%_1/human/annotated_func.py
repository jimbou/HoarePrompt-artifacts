#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `i` is `t-1`, `a`, `b`, `c` are integers between 0 and 9, `a`, `b`, `c` are assigned the values of the last line of stdin which contains three digits (0 <= a, b, c <= 9), stdin is empty. If `a` is less than `b` and `b` is less than `c`, then 'STAIRS' is printed. If `a` is less than `b` and `b` is greater than `c`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where the first line contains an integer t (1 <= t <= 1000) and each subsequent line contains three digits a, b, c (0 <= a, b, c <= 9). It then classifies each set of three digits into one of three categories: 'STAIRS' if a < b < c, 'PEAK' if a < b > c, or 'NONE' otherwise. The function prints the classification for each set of three digits.

