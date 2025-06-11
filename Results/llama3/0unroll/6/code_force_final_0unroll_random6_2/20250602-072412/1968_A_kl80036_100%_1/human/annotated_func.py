#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t space-separated integers x (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: stdin contains no inputs, and the console contains t lines of output, each containing the value of y (which is one less than the corresponding input value x).

#Overall this is what the function does:The function reads a series of integers from standard input, subtracts 1 from each integer, and prints the resulting values to the console. It processes a variable number of inputs, as specified by the first input value, and produces a corresponding number of output lines.

