#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: t is a string, x is a list containing ten integers, y is a list containing ten integers, i is 9, the range is defined as 10, stdin is empty
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: t is a string, x is a list containing ten integers, y is a list containing ten integers, i is 10, the range is defined as 10, stdin is empty. For all indices i in the range from 0 to 9, if x[i] is less than y[i], the values of x[i] and y[i] are printed. Otherwise, the values of y[i] and x[i] are printed.

#Overall this is what the function does:This function reads input from the standard input, expecting an integer t followed by t lines of two space-separated integers x and y. It then compares each pair of x and y, and prints the smaller value first, followed by the larger value. The function does not return any value, but instead prints the sorted pairs to the standard output.

