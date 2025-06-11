#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 1000) and then t lines each containing three digits (0 <= a, b, c <= 9).
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output will contain t lines, each containing either 'STAIR', 'PEAK', or 'NONE', depending on the values of a, b, and c in each line of the input. The value of t remains unchanged.

#Overall this is what the function does:This function reads a series of triple-digit numbers from standard input, classifies each triple as either 'STAIR', 'PEAK', or 'NONE' based on the relative values of the digits, and prints the classification for each triple. The function does not modify the input values or retain any information after execution.

