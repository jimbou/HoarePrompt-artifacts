#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: t is a string representing an integer between 1 and 100, x is a list of 10 integers between 0 and 9, y is a list of 10 integers between 0 and 9, stdin is empty.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: Output State: The output state is a string representing an integer between 1 and 100, x is a list of 10 integers between 0 and 9, y is a list of 10 integers between 0 and 9, stdin is empty, and the stdout contains 10 lines, each containing two integers between 0 and 9, separated by a space, where the first integer is the smaller of x[i] and y[i] and the second integer is the larger of x[i] and y[i].

#Overall this is what the function does:This function reads input from stdin, expecting an integer t (1 <= t <= 100) followed by t lines of two space-separated integers x and y (0 <= x, y <= 9). It then prints to stdout t lines, each containing the smaller and larger of the corresponding x and y values, separated by a space. The function does not return any value, and its primary purpose is to output the sorted pairs of integers.

