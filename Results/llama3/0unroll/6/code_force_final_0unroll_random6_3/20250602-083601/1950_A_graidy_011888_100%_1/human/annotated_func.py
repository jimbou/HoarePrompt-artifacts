#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output state will contain n lines, each containing one of the strings 'STAIR', 'PEAK', or 'NONE', depending on the values of a, b, and c in each line of the input. The values of n and the input lines remain unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t lines of input, each containing three digits a, b, and c. It then classifies each set of digits into one of three categories: 'STAIR' if a < b < c, 'PEAK' if a < b and b > c, or 'NONE' otherwise. The function prints the classification for each set of digits on a new line, resulting in t lines of output. The original input values remain unchanged.

