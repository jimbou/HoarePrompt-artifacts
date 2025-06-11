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
        
    #State: `t` is an integer (1 <= t <= 1000), stdin contains no lines. `i` is equal to `t`. `a`, `b`, `c` are integers between 0 and 9, and are the values of the three digits in the last line of stdin. If `a` is less than `b` and `b` is less than `c`, 'STAIR' is printed. If `a`, `b`, and `c` are all equal, 'NONE' is printed. If `a`, `b`, and `c` are not all equal, then if the maximum of `a`, `b`, and `c` is `b`, 'PEAK' is printed. Otherwise, 'NONE' is printed.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains three digits. It then classifies each set of three digits into one of four categories: 'STAIR' if the digits are in ascending order, 'PEAK' if the middle digit is the largest, 'NONE' if the digits are all equal, and 'NONE' otherwise. The classification of each set of digits is printed to the console. The function does not return any value.

