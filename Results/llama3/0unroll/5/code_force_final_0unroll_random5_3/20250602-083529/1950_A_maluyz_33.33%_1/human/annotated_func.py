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
        
    #State: The output will contain t lines, each containing one of the strings 'STAIR', 'NONE', or 'PEAK', depending on the values of a, b, and c in each line of the input. The value of t remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t lines of input, each containing three digits a, b, and c. It then classifies each set of digits into one of four categories: 'STAIR' if a < b < c, 'NONE' if a == b == c, 'PEAK' if the maximum value is b, or 'NONE' otherwise. The function prints the classification for each set of digits, resulting in t lines of output. The original value of t remains unchanged.

