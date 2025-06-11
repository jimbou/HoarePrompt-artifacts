#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b, where 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing and ends the execution. The values of n, m, x1, y1, x2, y2, and r remain unchanged. The current value of x2 is still less than or equal to the current value of x1, and 'draw' is still being printed. The stdin still contains multiple test cases minus one.
    #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, and x2 is larger than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing, but 'Alice' has been printed. The current state of variables remains unchanged: n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, x2 is larger than x1, and the difference between x2 and x1 is an odd number. The current value of y1 is equal to the current value of y2.
        #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, x2 is larger than x1, and the difference between x2 and x1 is an odd number, y1 is not equal to y2
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing, as there is no return statement with a value. The values of n, m, x1, y1, x2, y2, and r remain unchanged. The difference between x2 and x1 is still even, and y1 and y2 are still equal. The program has printed 'bob' to the standard output.
        #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, x2 is larger than x1, the difference between x2 and x1 is even, and y1 is not equal to y2

#Overall this is what the function does:Determines the winner of a game based on the positions of two players, Alice and Bob, on a grid. The function takes no arguments and reads input from stdin, which contains multiple test cases. Each test case consists of six integers: the height and width of the grid, and the x and y coordinates of Alice and Bob. The function prints 'draw' if Alice's x-coordinate is less than or equal to Bob's x-coordinate, 'Alice' if the difference between their x-coordinates is odd and their y-coordinates are equal, or 'Bob' if the difference between their x-coordinates is even and their y-coordinates are equal. The function returns nothing and ends execution after printing the result.

