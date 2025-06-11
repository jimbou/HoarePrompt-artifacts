#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b. h and w are positive integers, 1 <= x_a, x_b <= h, 1 <= y_a, y_b <= w.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing, as there is no explicit return statement. The program simply ends without producing any output or returning any value.
    #State: *n is a positive integer, m is a positive integer, x1 is a positive integer between 1 and n, y1 is a positive integer between 1 and m, x2 is a positive integer between 1 and n, y2 is a positive integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one. x2 is larger than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing, as there is no explicit return statement. The state of the variables remains the same: n and m are positive integers, x1 and x2 are positive integers between 1 and n, y1 and y2 are positive integers between 1 and m, x2 is larger than x1, (x2 - x1) is an odd number, y1 is equal to y2, and 'Alice' has been printed. The list r still contains six integers, and stdin still contains multiple test cases minus one.
        #State: *n is a positive integer, m is a positive integer, x1 is a positive integer between 1 and n, y1 is a positive integer between 1 and m, x2 is a positive integer between 1 and n, y2 is a positive integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one. x2 is larger than x1. The current value of (x2 - x1) is an odd number. y1 is not equal to y2
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing because there is no value or variable specified in the return statement. The program ends without providing any output.
        #State: *n is a positive integer, m is a positive integer, x1 is a positive integer between 1 and n, y1 is a positive integer between 1 and m, x2 is a positive integer between 1 and n, y2 is a positive integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one. x2 is larger than x1. The difference between x2 and x1 is even. y1 and y2 are not equal

#Overall this is what the function does:Determines the winner of a game based on the input coordinates and prints the result. The function takes no parameters and returns no value. It reads six integers from standard input, representing the dimensions of a game board and the coordinates of two players. If the x-coordinates of the two players are equal, the function prints 'draw'. Otherwise, it checks if the difference between the x-coordinates is odd or even and if the y-coordinates are equal. Based on these conditions, it prints either 'Alice' or 'Bob' to indicate the winner. The function does not modify the input values or return any result, only printing the outcome of the game to the console.

