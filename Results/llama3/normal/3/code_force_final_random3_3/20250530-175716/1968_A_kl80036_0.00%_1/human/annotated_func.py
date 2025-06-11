#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) (1 <= t <= 1000) and then t lines each containing an integer (x) (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: x is an integer between 2 and 1000, y is an integer equal to x // 2, i is t-1, stdin contains 0 inputs, and the value of y which is equal to x // 2 is being printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer (t) specifies the number of subsequent integers to read. For each of these integers (x), it calculates and prints the integer division of x by 2. The function continues this process until all specified integers have been read and processed, at which point it concludes, leaving the standard input empty.

