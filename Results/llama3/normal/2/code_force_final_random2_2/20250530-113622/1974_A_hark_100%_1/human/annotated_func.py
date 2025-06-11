#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 10^4), the following t inputs are two space-separated integers x and y (0 <= x, y <= 99).
    ap = int(input())
    for k in range(ap):
        x, y = map(int, input().split())
        
        if x > 0 and y > 0:
            bxsfory = math.ceil(y / 2)
            x = x - bxsfory * 15 + y * 4
            bxsfory1 = 0 if x <= 0 else math.ceil(x / 15)
            print(bxsfory1 + bxsfory)
        elif x == 0 and y > 0:
            print(math.ceil(y / 2))
        elif x > 0 and y == 0:
            print(math.ceil(x / 15))
        else:
            print(0)
        
    #State: `ap` is an integer between 0 and 10^4, `k` is `ap`, `x` is an integer between -1485 and 99, `y` is an integer between 0 and 99, stdin contains no input. If `x` > 0 and `y` > 0, the sum of `bxsfory1` and `bxsfory` is printed, which is an integer between 0 and 58. If `x` is 0 and `y` is positive, the ceiling of `y` divided by 2 is printed. If `x` is positive and `y` is 0, the smallest integer not less than `x` divided by 15 is printed. Otherwise, 0 is printed.

#Overall this is what the function does:This function reads a series of inputs from stdin, where the first input is an integer t, and the following t inputs are pairs of integers x and y. For each pair, it calculates and prints a value based on the values of x and y. If both x and y are positive, it calculates the sum of the ceiling of y divided by 2 and the ceiling of x minus the product of the ceiling of y divided by 2 and 15, plus the product of y and 4, divided by 15. If x is 0 and y is positive, it prints the ceiling of y divided by 2. If x is positive and y is 0, it prints the ceiling of x divided by 15. If both x and y are 0, it prints 0. The function processes all input pairs and then terminates, leaving stdin empty.

