#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 1000) and then t lines each containing three space-separated digits (0 <= a, b, c <= 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output state will contain t lines, each containing one of the strings 'STAIR', 'PEAK', or 'NONE', depending on the values of a, b, and c in each line of the input. The value of t remains unchanged.

#Overall this is what the function does:This function reads a series of input lines from standard input, where the first line contains an integer t (1 <= t <= 1000) representing the number of test cases, and each subsequent line contains three space-separated digits (0 <= a, b, c <= 9). It then classifies each set of three digits into one of three categories: 'STAIR' if a < b < c, 'PEAK' if a < b > c, or 'NONE' otherwise. The function prints the classification for each set of digits on a separate line, resulting in a total of t output lines. The original value of t remains unchanged.

