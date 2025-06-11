#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Each test case consists of a single line containing six integers h, w, x_a, y_a, x_b, y_b (1 ≤ x_a, x_b ≤ h ≤ 10^6, 1 ≤ y_a, y_b ≤ w ≤ 10^9) — the dimensions of the board and the initial positions of Alice's and Bob's chips. It is guaranteed that either x_a ≠ x_b or y_a ≠ y_b.
    r = list(map(int, input().split()))
    n, m, x1, y1, x2, y2 = r[0], r[1], r[2], r[3], r[4], r[5]
    if (x2 <= x1) :
        print('draw')
        #This is printed: draw
        return
        #The program returns nothing
    #State: *n is an integer between 1 and 10^4, m is an integer between 1 and 10^6, x1 is an integer between 1 and 10^6, y1 is an integer between 1 and 10^9, x2 is an integer between 1 and 10^6, y2 is an integer between 1 and 10^9, r is a list of six integers, stdin contains multiple test cases minus one. x2 is larger than x1
    if ((x2 - x1) % 2 != 0) :
        if (y1 == y2) :
            print('Alice')
            #This is printed: Alice
            return
            #The program returns nothing because there is no return statement with a value. The program ends without returning any value.
        #State: *n is an integer between 1 and 10^4, m is an integer between 1 and 10^6, x1 is an integer between 1 and 10^6, y1 is an integer between 1 and 10^9, x2 is an integer between 1 and 10^6, y2 is an integer between 1 and 10^9, r is a list of six integers, stdin contains multiple test cases minus one. The current value of x2 is larger than x1. The difference between x2 and x1 is an odd number. y1 is not equal to y2
    else :
        if (y1 == y2) :
            print('bob')
            #This is printed: bob
            return
            #The program returns nothing and 'bob' is still being printed, and the values of n, m, x1, y1, x2, y2, and r remain unchanged. The difference between x2 and x1 is still even, and y1 is still equal to y2.
        #State: *n is an integer between 1 and 10^4, m is an integer between 1 and 10^6, x1 is an integer between 1 and 10^6, y1 is an integer between 1 and 10^9, x2 is an integer between 1 and 10^6, y2 is an integer between 1 and 10^9, r is a list of six integers, stdin contains multiple test cases minus one. x2 is larger than x1, the difference between x2 and x1 is even, and y1 is not equal to y2

#Overall this is what the function does:Determines the winner of a game based on the positions of two chips on a board. The function takes no parameters and returns nothing. It reads input from stdin, which contains multiple test cases, each consisting of six integers representing the dimensions of the board and the initial positions of the chips. The function prints the result of each test case, either 'draw', 'Alice', or 'Bob', depending on the relative positions of the chips. The function does not modify the input variables and does not return any value.

