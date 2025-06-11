#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 ≤ t ≤ 1000) and then t space-separated integers (2 ≤ x ≤ 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: stdin contains no inputs, and the console contains t lines of output, each containing the integer division of the corresponding input integer by 2.

#Overall this is what the function does:Reads a series of integers from standard input, performs integer division by 2 on each number, and prints the results to the console, consuming all input and producing a corresponding number of output lines.

