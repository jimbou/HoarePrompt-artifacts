#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a == b == c:
            print('NONE')
        elif max(a, b, c) == b:
            print('PEAK')
        else:
            print('NONE')
        
    #State: `t` is an integer between 1 and 1000 (inclusive), `i` is `t-1`, `a`, `b`, `c` are integers between 0 and 9 (inclusive), and are the values of the last line of input from stdin, stdin is empty. If `a` < `b` < `c`, then 'STAIR' is printed. Otherwise, if `a`, `b`, and `c` are equal, then 'NONE' is printed. Otherwise, if the maximum value among `a`, `b`, and `c` is `b`, then 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:The function reads a series of lines from standard input, where each line contains three digits. It then classifies each set of three digits into one of four categories: 'STAIR' if the digits are in strictly increasing order, 'PEAK' if the middle digit is the largest, 'NONE' if all digits are equal, and 'NONE' otherwise. The classification is printed to the console for each set of three digits. The function does not return any value and does not modify the input variables.

