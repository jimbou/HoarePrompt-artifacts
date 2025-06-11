#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing three digits a, b, c (0 <= a, b, c <= 9).
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
        
    #State: The output state will contain t lines, each containing one of the strings 'STAIR', 'NONE', or 'PEAK', depending on the values of a, b, and c in each line of the input.

#Overall this is what the function does:This function reads a series of inputs from stdin, where the first input is an integer t, followed by t lines each containing three digits a, b, and c. It then analyzes each set of three digits and prints one of three possible strings: 'STAIR' if the digits are in ascending order, 'PEAK' if the middle digit is the largest, or 'NONE' in all other cases. The function outputs t lines, each containing one of these strings, depending on the input values.

