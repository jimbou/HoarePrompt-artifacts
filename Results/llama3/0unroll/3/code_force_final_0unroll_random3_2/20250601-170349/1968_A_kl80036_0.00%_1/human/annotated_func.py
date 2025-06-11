#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing a single integer x (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: stdin contains no more inputs and the console contains t lines each containing a single integer y (1 <= y <= 500).

#Overall this is what the function does:Reads a series of integers from standard input, divides each integer by 2, and prints the result to the console. The function consumes all input from standard input and produces a corresponding number of lines of output, each containing a single integer.

