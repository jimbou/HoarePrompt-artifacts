#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= integer <= 1000) and then a sequence of 3 space-separated integers (0 <= integer <= 9) repeated integer times.
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The output state will be a sequence of n lines, where each line contains one of the strings 'STAIR', 'PEAK', or 'NONE', depending on the values of a, b, and c in each iteration of the loop. The values of n and the input sequence remain unchanged.

#Overall this is what the function does:The function reads an integer n from the standard input, followed by n sequences of three space-separated integers. It then classifies each sequence as 'STAIR', 'PEAK', or 'NONE' based on the relative values of the integers and prints the classification for each sequence. The function does not modify the input values and produces a sequence of n lines as output, each containing one of the three classification strings.

