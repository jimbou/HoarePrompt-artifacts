#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The value of x is between 1 and 100 inclusive, and the values of x and y in each of the t-1 lines of stdin are swapped if they were in descending order, otherwise they remain unchanged.

#Overall this is what the function does:Reads an integer t from standard input, followed by t lines of two space-separated integers x and y. For each line, if x is greater than or equal to y, it prints the swapped values of x and y; otherwise, it prints the original values of x and y.

