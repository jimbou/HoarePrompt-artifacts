#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 100) and then t lines, each containing two space-separated integers (0 <= x, y <= 9).
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: t is a string containing an integer between 1 and 100, x is a list of 10 integers between 0 and 9, y is a list of 10 integers between 0 and 9, stdin is empty.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: Output State: t is a string containing an integer between 1 and 100, x is a list of 10 integers between 0 and 9, y is a list of 10 integers between 0 and 9, stdin is empty, and the console output contains 10 lines, each containing two integers between 0 and 9 separated by a space, where the first integer is the smaller of x[i] and y[i] and the second integer is the larger of x[i] and y[i] for each i between 0 and 9.

#Overall this is what the function does:This function reads input from the standard input, expecting an integer t between 1 and 100, followed by t lines of two space-separated integers x and y between 0 and 9. It then prints 10 lines to the console, each containing two integers: the smaller of x[i] and y[i] followed by the larger of x[i] and y[i] for each i between 0 and 9. The function does not return any value, and its purpose is to output the sorted pairs of integers read from the input.

