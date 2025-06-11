#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) (1 <= t <= 1000) and then t integers (x) (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: i is equal to t-1, stdin is empty, and y which is half of the (t-1)th input from stdin is being printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer (t) specifies the number of subsequent integers to read. It then calculates and prints half of each of these subsequent integers. The function continues this process until all specified integers have been read and processed, leaving the standard input empty.

