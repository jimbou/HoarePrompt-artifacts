#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 99).
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
        
    #State: `ap` is an integer between 1 and 10^4, stdin contains `ap` inputs: each containing two space-separated integers x and y (0 <= x, y <= 99), `k` is `ap` - 1, `x` and `y` are integers that are input by the user from stdin. If both `x` and `y` are greater than 0, then `bxsfory` is the ceiling of `y` divided by 2, `x` is `y` times 4 minus `bxsfory` times 15, `bxsfory1` is 0 if `x` is less than or equal to 0, otherwise it is the ceiling of `x` divided by 15, and `bxsfory1` + `bxsfory` is printed. If `x` is 0 and `y` is greater than 0, the ceiling of `y` divided by 2 is printed. If `x` is greater than 0 and `y` equals 0, the ceiling of the division of `x` by 15 is printed. Otherwise, the number 0 is printed.

#Overall this is what the function does:This function reads a series of input pairs from the standard input, where each pair consists of two integers x and y. It then performs calculations based on the values of x and y, and prints the results. If both x and y are positive, it calculates the ceiling of y divided by 2, subtracts this value multiplied by 15 from x, adds y multiplied by 4, and prints the sum of the ceiling of the result divided by 15 and the ceiling of y divided by 2. If x is 0 and y is positive, it prints the ceiling of y divided by 2. If x is positive and y is 0, it prints the ceiling of x divided by 15. If both x and y are 0, it prints 0. The function repeats this process for a number of input pairs specified by the first input, which is an integer between 1 and 10^4.

