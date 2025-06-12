#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of six space-separated integers: h, w, x_a, y_a, x_b, y_b, where 1 <= x_a, x_b <= h <= 10^6 and 1 <= y_a, y_b <= w <= 10^9.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing because there is no value or variable specified in the return statement.
    #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, stdin contains multiple test cases minus one, and x2 is greater than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing, as the return statement is empty. The values of n, m, x1, y1, x2, and y2 remain unchanged, with x2 being greater than x1, and y1 and y2 being equal. The program also still contains multiple test cases minus one in stdin, and 'Alice' has been printed.
        #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, stdin contains multiple test cases minus one, x2 is greater than x1, and the current value of (x2 - x1) is odd. Additionally, y1 is not equal to y2.
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing, but the current values of y1 and y2 are equal, and 'bob' has been printed. The difference between x2 and x1 is even, and x2 is greater than x1. The values of n, m, x1, y1, x2, and y2 remain unchanged within their respective ranges.
        #State: *n is an integer between 1 and 10^6, m is an integer between 1 and 10^9, x1 is an integer between 1 and n, y1 is an integer between 1 and m, x2 is an integer between 1 and n, y2 is an integer between 1 and m, stdin contains multiple test cases minus one, x2 is greater than x1, the difference between x2 and x1 is even, and y1 is not equal to y2

#Overall this is what the function does:This function determines the winner of a game based on the input values of h, w, x_a, y_a, x_b, and y_b, representing the height, width, and coordinates of two players. It reads input from stdin, processes one test case at a time, and prints the result ('draw', 'Alice', or 'bob') based on the relative positions of the players. The function does not return any value and does not modify the input values. It only prints the result and consumes one test case from stdin.

