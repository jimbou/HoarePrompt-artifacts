#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 1000) and then a sequence of lines, each containing three digits (between 0 and 9).
    q = int(input())
    for i in range(q):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output will be a sequence of lines, each containing either 'STAIR', 'PEAK', or 'NONE', depending on the values of a, b, and c in each iteration. The number of lines will be equal to the value of q. The value of q will be unchanged.

#Overall this is what the function does:The function reads an integer q from standard input, followed by q sequences of three digits each. It then classifies each sequence as 'STAIR', 'PEAK', or 'NONE' based on the relative values of the digits and prints the classification for each sequence. The function does not modify the input values and produces q lines of output.

