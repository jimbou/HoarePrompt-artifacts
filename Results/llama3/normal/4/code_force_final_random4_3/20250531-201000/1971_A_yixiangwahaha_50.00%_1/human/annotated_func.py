#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: x is a list containing ten integers, y is a list containing ten integers, stdin contains 0 inputs, t is a string, i is 9
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: x is a list containing ten integers, y is a list containing ten integers, stdin contains 0 inputs, t is a string, i is 9, the number 10 is greater than or equal to 10. The elements of the lists x and y have been printed in ascending order for all ten iterations.

#Overall this is what the function does:The function reads two integers from standard input for ten iterations, stores them in separate lists, and then prints each pair of integers in ascending order. The function does not return any value but modifies the standard output by printing the sorted pairs. The function assumes that the input is well-formed and does not perform any error checking.

