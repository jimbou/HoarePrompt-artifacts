#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: x is a list containing ten integers, y is a list containing ten integers, i is 9, stdin is empty
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `x` and `y` are lists containing ten integers, `i` is 10, `10` is not greater than 10, and stdin is empty. The first ten elements of `x` and `y` are compared, and the smaller value is printed first, followed by the larger value.

#Overall this is what the function does:This function reads input from stdin, expecting an integer t (1 <= t <= 100) followed by t lines of two space-separated integers x and y (0 <= x, y <= 9). It then compares each pair of x and y values, printing the smaller value first, followed by the larger value. The function does not return any value but prints the results directly to the console.

