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
        
    #State: `t` is an integer between 0 and 1000, `i` is `t`, stdin is empty.

#Overall this is what the function does:The function reads a series of lines from standard input, where each line contains three digits. It then classifies each set of three digits into one of four categories: 'STAIR' if the digits are in strictly increasing order, 'PEAK' if the middle digit is the largest, 'NONE' if the digits are all equal, and 'NONE' otherwise. The classification of each set of digits is printed to the console. The function consumes all input from standard input and leaves the input stream empty.

