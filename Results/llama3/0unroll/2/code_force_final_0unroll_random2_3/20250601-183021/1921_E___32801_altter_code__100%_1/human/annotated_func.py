#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six integers h, w, x_a, y_a, x_b, y_b, where 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. The first integer t (1 <= t <= 10^4) represents the number of test cases.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing because the return statement is empty.
    #State: *n is an integer between 1 and 10^4, m is an integer between 1 and 10^6, x1 is an integer between 1 and 10^6, y1 is an integer between 1 and 10^9, x2 is an integer between 1 and 10^6, y2 is an integer between 1 and 10^9, r is a list of six integers, stdin contains multiple test cases minus one, and x2 is larger than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing, as the return statement is empty. The values of n, m, x1, y1, x2, y2, and r remain unchanged. The difference between x2 and x1 is still odd, and y1 and y2 are still equal. The program has printed 'Alice' to the standard output. The stdin still contains multiple test cases minus one.
        #State: *n is an integer between 1 and 10^4, m is an integer between 1 and 10^6, x1 is an integer between 1 and 10^6, y1 is an integer between 1 and 10^9, x2 is an integer between 1 and 10^6, y2 is an integer between 1 and 10^9, r is a list of six integers, stdin contains multiple test cases minus one, and x2 is larger than x1. The current value of (x2 - x1) is odd. y1 is not equal to y2
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing, as there is no explicit return statement with a value. The program simply ends after printing 'bob' and processing the test cases. The values of n, m, x1, y1, x2, y2, and r remain unchanged, and the difference between x2 and x1 remains even. The current value of y1 remains equal to the current value of y2.
        #State: *n is an integer between 1 and 10^4, m is an integer between 1 and 10^6, x1 is an integer between 1 and 10^6, y1 is an integer between 1 and 10^9, x2 is an integer between 1 and 10^6, y2 is an integer between 1 and 10^9, r is a list of six integers, stdin contains multiple test cases minus one, x2 is larger than x1, the difference between x2 and x1 is even, and y1 is not equal to y2

#Overall this is what the function does:This function determines the winner of a game based on the input values of h, w, x_a, y_a, x_b, and y_b, where h and w represent the dimensions of a grid, and x_a, y_a, x_b, and y_b represent the positions of two players. The function prints 'draw' if x_b is less than or equal to x_a, 'Alice' if the difference between x_b and x_a is odd and y_a is equal to y_b, and 'bob' if the difference between x_b and x_a is even and y_a is equal to y_b. In all cases, the function does not return any value.

