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
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `i` is `t-1`, `a`, `b`, and `c` are integers between 0 and 9 (inclusive), `a`, `b`, and `c` are the three digits from the last line of the standard input, and the standard input is empty. If `a` is less than `b` and `b` is less than `c`, then 'STAIR' is printed. If `a` is less than `b` and `b` is greater than `c`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains three digits. It then classifies each set of three digits as either 'STAIR', 'PEAK', or 'NONE' based on their relative values and prints the classification. The function processes a specified number of lines (between 1 and 1000), and after processing all lines, the standard input is empty.

