#State of the program right berfore the function call: a and b are non-negative integers.
    return a if a < b else b
    #The program returns the smaller of the two non-negative integers, a and b.

#Overall this is what the function does:The function compares two non-negative integers, a and b, and returns the smaller of the two.

#State of the program right berfore the function call: stdin contains one input: two space-separated integers x and y such that 0 <= x <= 99 and 0 <= y <= 99.
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: an integer between 1 and 57 (which is the sum of bxsfory1 and bxsfory)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: the smallest integer greater than or equal to half of y
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: an integer between 1 and 7 (inclusive), which is the ceiling of x/15
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are integers between 0 and 99, stdin contains no input. Either `x` is 0, or `y` is 0, or both `x` and `y` are 0. It is not the case that `x` is 0 and `y` is greater than 0. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is being printed. Otherwise, the number 0 is being printed.
        #State: *`x` and `y` are integers between 0 and 99, stdin contains no input. Either `x` is 0, or `y` is 0, or both `x` and `y` are 0. If `x` is 0 and `y` is greater than 0, the ceiling of y divided by 2 is being printed. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is being printed. Otherwise, the number 0 is being printed.
    #State: *`x` and `y` are integers between 0 and 99, stdin contains no input. If both `x` and `y` are greater than 0, the sum of bxsfory1 and bxsfory is being printed, where bxsfory1 is an integer between 0 and 7, bxsfory is an integer between 1 and 50, and the sum is an integer between 1 and 57. If `x` is 0 and `y` is greater than 0, the ceiling of y divided by 2 is being printed. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is being printed. Otherwise, the number 0 is being printed.

#Overall this is what the function does:Calculates and prints a value based on the input integers x and y. If both x and y are greater than 0, it calculates the sum of bxsfory1 and bxsfory, where bxsfory1 is the ceiling of x divided by 15 plus 1, and bxsfory is the ceiling of y divided by 2. If x is 0 and y is greater than 0, it prints the ceiling of y divided by 2. If x is greater than 0 and y is 0, it prints the ceiling of x divided by 15. If both x and y are 0, it prints 0. The function consumes the input from stdin and leaves it empty.

#State of the program right berfore the function call: stdin contains one input: an integer t (1 <= t <= 10^4)
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: The output state after the loop executes all the iterations is: `t` is an integer between 1 and 10^4 (inclusive), stdin contains no input.

#Overall this is what the function does:The function reads an integer `t` from standard input, where `t` is between 1 and 10^4 (inclusive), and then calls another function `func_2()` `t` times. After all iterations, the function leaves the standard input empty.

