#State of the program right berfore the function call: a and b are non-negative integers.
    return a if a < b else b
    #The program returns the smaller of the two non-negative integers a and b.

#Overall this is what the function does:This function compares two non-negative integers, a and b, and returns the smaller of the two.

#State of the program right berfore the function call: stdin contains one input: two space-separated integers x and y, where x and y are non-negative integers less than or equal to 99.
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory1 and bxsfory are positive integers)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: the ceiling of the division of y by 2 (where y is a non-negative integer less than or equal to 99 and greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: the smallest integer not less than x / 15 (where x is the current value of x, which is greater than 0 and less than or equal to 99)
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are non-negative integers less than or equal to 99, stdin is empty. Either `x` is 0 or `y` is 0 or both are 0. It is not the case that `x` is 0 and `y` is greater than 0. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.
        #State: *`x` and `y` are non-negative integers less than or equal to 99, stdin is empty. Either `x` is 0 or `y` is 0 or both are 0. If `x` is 0 and `y` is greater than 0, the ceiling of half of the value of `y` is printed. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.
    #State: *`x` and `y` are non-negative integers less than or equal to 99, stdin is empty. If both `x` and `y` are greater than 0, the sum of bxsfory1 and bxsfory is printed. If either `x` is 0 or `y` is 0 or both are 0, then if `x` is 0 and `y` is greater than 0, the ceiling of half of the value of `y` is printed. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.

#Overall this is what the function does:This function reads two non-negative integers x and y from standard input, where x and y are less than or equal to 99. It then performs calculations based on the values of x and y. If both x and y are greater than 0, it calculates and prints the sum of two positive integers, bxsfory1 and bxsfory. If either x is 0 or y is 0 or both are 0, it prints either the ceiling of half of y (if x is 0 and y is greater than 0), the ceiling of the division of x by 15 (if x is greater than 0 and y is 0), or 0 (in all other cases). The function does not return any value, but it prints the calculated result to the standard output.

#State of the program right berfore the function call: stdin contains one input: an integer t (1 <= t <= 10^4)
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` is an integer between 1 and 10^4, `_` is `t-1`, and the function `func_2()` has been executed `t` times.

#Overall this is what the function does:The function reads an integer `t` from standard input and executes the function `func_2()` `t` times, where `t` is between 1 and 10^4.

