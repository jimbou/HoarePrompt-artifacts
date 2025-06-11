#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: stdin contains an empty string, t is a string, x is a list containing 10 integers, y is a list containing 10 integers.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: Output State: The stdin contains an empty string, t is a string, x is a list containing 10 integers, y is a list containing 10 integers.

#Overall this is what the function does:This function reads input from stdin, expecting an integer t followed by t lines of two space-separated integers x and y. It then prints the pairs of integers in ascending order, swapping the positions of x and y if necessary. The function does not return any value, and its purpose is to output the sorted pairs of integers to the console.

