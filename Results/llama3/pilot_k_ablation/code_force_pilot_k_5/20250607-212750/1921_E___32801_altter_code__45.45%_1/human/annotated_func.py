#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains six space-separated integers: h, w, x_a, y_a, x_b, y_b. 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9. x_a != x_b or y_a != y_b.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing, as the return statement is empty. The current state of the variables remains unchanged, with 'n' being an integer between 1 and 10^6, 'm' being an integer between 1 and 10^9, 'x1' being an integer between 1 and 'n', 'y1' being an integer between 1 and 'm', 'x2' being an integer between 1 and 'n' and less than or equal to 'x1', 'y2' being an integer between 1 and 'm', and 'r' being a list of six integers. Additionally, 'draw' is still printed, and the stdin contains multiple test cases minus one.
    #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, and x2 is greater than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing because the return statement is empty, and the current state of the variables remains unchanged. The value of n is still an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, x2 is greater than x1, and the difference between x2 and x1 is an odd number. Additionally, the current value of y1 is equal to the current value of y2, and 'Alice' is printed.
        #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, x2 is greater than x1, the difference between x2 and x1 is an odd number, and y1 is not equal to y2
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing, as there is no explicit return statement. The program simply ends without returning any value.
        #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, r is a list of six integers, stdin contains multiple test cases minus one, x2 is greater than x1, the difference between x2 and x1 is even, and y1 is not equal to y2

#Overall this is what the function does:Determines the winner of a game based on the input coordinates and prints the result. The function takes no arguments and uses the input from the standard input. It reads six space-separated integers representing the height, width, and coordinates of two points. If the x-coordinates are equal, it prints 'draw'. If the difference between the x-coordinates is odd, it prints 'Alice' if the y-coordinates are equal, otherwise, it prints 'bob'. If the difference between the x-coordinates is even, it prints 'bob' if the y-coordinates are equal, otherwise, it prints 'Alice'. The function returns no value and modifies no external state, only printing the result to the standard output.

