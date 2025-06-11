#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines, each containing three digits a, b, c (0 <= a, b, c <= 9).
    q = int(input())
    mn = 100
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        
        if a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: Output State: The loop will print out 'STAIR', 'PEAK', or 'NONE' for each line of input, depending on the values of a, b, and c. The value of q will be 0, and the value of mn will remain 100. The stdin will be empty.

#Overall this is what the function does:This function reads a series of input lines from standard input, where each line contains three digits. It then classifies each set of digits as 'STAIR', 'PEAK', or 'NONE' based on their relative values and prints out the classification for each set. The function does not return any value or modify any external state, but instead, produces output directly to the console.

