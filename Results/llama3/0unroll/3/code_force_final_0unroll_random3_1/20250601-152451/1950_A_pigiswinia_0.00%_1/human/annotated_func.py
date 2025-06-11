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
        
    #State: The output will contain `t` lines, each containing either 'STAIRS', 'PEAK', or 'NONE', depending on the values of `a`, `b`, and `c` in each line of the input.

#Overall this is what the function does:This function reads a series of lines from standard input, where each line contains three digits. It then classifies each set of digits into one of three categories: 'STAIRS' if the digits are in strictly increasing order, 'PEAK' if the second digit is greater than both the first and third, and 'NONE' otherwise. The classification for each set of digits is printed to standard output.

