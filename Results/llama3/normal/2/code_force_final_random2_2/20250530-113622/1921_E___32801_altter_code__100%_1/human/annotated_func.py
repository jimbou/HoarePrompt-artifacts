#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 10^4) — the number of test cases. Each test case consists of a single line containing six integers h, w, x_a, y_a, x_b, y_b (1 <= x_a, x_b <= h <= 10^6, 1 <= y_a, y_b <= w <= 10^9) — the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a != x_b or y_a != y_b.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing, 'draw' is printed, and the values of n, m, x1, y1, x2, and y2 remain unchanged.
    #State: stdin contains multiple test cases minus one, n is an integer, m is an integer, x1 is an integer, y1 is an integer, x2 is an integer, y2 is an integer, and x2 is greater than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing
        #State: *stdin contains multiple test cases minus one, n is an integer, m is an integer, x1 is an integer, y1 is an integer, x2 is an integer, y2 is an integer, x2 is greater than x1, the difference between x2 and x1 is an odd number, and y1 is not equal to y2
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing and 'bob' is printed, the difference between x2 and x1 is even, and the current values of y1 and y2 are equal.
        #State: *stdin contains multiple test cases minus one, n is an integer, m is an integer, x1 is an integer, y1 is an integer, x2 is an integer, y2 is an integer, x2 is greater than x1, the difference between x2 and x1 is even, and y1 is not equal to y2

#Overall this is what the function does:Determines the winner of a game based on the positions of two chips on a board, printing 'draw' if the chips are in the same position, 'Alice' if the difference between the x-coordinates is odd and the y-coordinates are different, or 'Bob' if the difference between the x-coordinates is even and the y-coordinates are the same.

