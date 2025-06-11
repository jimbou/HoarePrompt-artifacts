#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output will contain q lines, each containing one of the strings 'STAIR', 'PEAK', or 'NONE', depending on the values of a, b, and c in each line of the input.

#Overall this is what the function does:This function reads an integer t from standard input, followed by t lines of input, each containing three digits a, b, and c. It then classifies each triplet as 'STAIR', 'PEAK', or 'NONE' based on the relative values of a, b, and c, and prints the classification for each triplet. The function does not return any value but produces output for each input triplet.

