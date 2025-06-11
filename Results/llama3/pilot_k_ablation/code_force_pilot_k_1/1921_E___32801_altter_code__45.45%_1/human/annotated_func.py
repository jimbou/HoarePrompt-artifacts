#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers: h, w, x_a, y_a, x_b, y_b. h and w are positive integers (1 <= h <= 10^6, 1 <= w <= 10^9). x_a, y_a, x_b, y_b are positive integers (1 <= x_a, x_b <= h, 1 <= y_a, y_b <= w). x_a != x_b or y_a != y_b.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing, as there is no explicit return statement. The program ends without returning any value.
    #State: *n is a positive integer between 1 and 10^6, m is a positive integer between 1 and 10^9, x1 is a positive integer between 1 and n, y1 is a positive integer between 1 and m, x2 is a positive integer between 1 and n, y2 is a positive integer between 1 and m, stdin contains multiple test cases minus one, r is a list of six integers. x2 is larger than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing because there is no return value specified in the code snippet. The values of n, m, x1, y1, x2, and y2 remain unchanged. The difference between x2 and x1 is still an odd number, and y1 and y2 are still equal. The program has printed 'Alice' to the standard output.
        #State: *n is a positive integer between 1 and 10^6, m is a positive integer between 1 and 10^9, x1 is a positive integer between 1 and n, y1 is a positive integer between 1 and m, x2 is a positive integer between 1 and n, y2 is a positive integer between 1 and m, stdin contains multiple test cases minus one, r is a list of six integers. The current value of x2 is larger than x1 and the difference between x2 and x1 is an odd number. y1 is not equal to y2.
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing and 'bob' is printed. The values of n, m, x1, y1, x2, and y2 remain unchanged. The difference between x2 and x1 is still even. y1 is still equal to y2.
        #State: *n is a positive integer between 1 and 10^6, m is a positive integer between 1 and 10^9, x1 is a positive integer between 1 and n, y1 is a positive integer between 1 and m, x2 is a positive integer between 1 and n, y2 is a positive integer between 1 and m, stdin contains multiple test cases minus one, r is a list of six integers. x2 is larger than x1. The difference between x2 and x1 is even. y1 is not equal to y2

#Overall this is what the function does:Determines the winner of a game based on the positions of two players, Alice and Bob, on a grid. The function takes no parameters but reads six integers from standard input: the height and width of the grid, and the x and y coordinates of Alice and Bob. It then prints the winner of the game ('Alice', 'Bob', or 'draw') based on the relative positions of the players and the parity of the difference between their x-coordinates. The function does not return any value and only prints the result to the standard output.

