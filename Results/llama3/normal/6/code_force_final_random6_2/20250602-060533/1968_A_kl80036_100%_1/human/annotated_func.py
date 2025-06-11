#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 1000) and the remaining t inputs are integers x (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: i is an integer equal to t, x is an integer equal to the last input value, y is an integer equal to x - 1, stdin contains no input, and the value of y which is equal to x - 1 is being printed.

#Overall this is what the function does:Reads a series of integers from standard input, where the first integer t represents the number of subsequent integers, and for each integer x, prints the value of x - 1.

