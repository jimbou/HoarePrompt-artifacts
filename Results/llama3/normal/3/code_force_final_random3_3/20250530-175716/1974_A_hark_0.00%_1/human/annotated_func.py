#State of the program right berfore the function call: a and b are non-negative integers.
    return a if a < b else b
    #The program returns the smaller of the two non-negative integers a and b.

#Overall this is what the function does:The function compares two non-negative integers, a and b, and returns the smaller of the two.

#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 10^4) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 99).
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: a value between 1 and 57 (which is the sum of bxsfory1 and bxsfory)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: the ceiling of the division of y by 2 (where y is an integer between 0 and 99 and the current value of y is greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: the smallest integer not less than x divided by 15 (where x is an integer between 1 and 99)
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are integers between 0 and 99, stdin contains one input: an integer t (1 <= t <= 10^4) and then t-1 lines each containing two space-separated integers x and y (0 <= x, y <= 99). Either `x` is 0 or `y` is 0 or both are 0. Additionally, it is not the case that `x` is 0 and `y` is greater than 0. If `x` is greater than 0 and `y` is 0, the ceiling of x divided by 15 is being printed. Otherwise, 0 is being printed.
        #State: *`x` and `y` are integers between 0 and 99, stdin contains one input: an integer t (1 <= t <= 10^4) and then t-1 lines each containing two space-separated integers x and y (0 <= x, y <= 99). Either `x` is 0 or `y` is 0 or both are 0. If `x` is 0 and `y` is greater than 0, the ceiling of half of the value of `y` is being printed. If `x` is greater than 0 and `y` is 0, the ceiling of x divided by 15 is being printed. Otherwise, 0 is being printed.
    #State: *`x` and `y` are integers between 0 and 99, stdin contains one input: an integer t (1 <= t <= 10^4) and then t-1 lines each containing two space-separated integers x and y (0 <= x, y <= 99). If both `x` and `y` are greater than 0, the sum of bxsfory1 and bxsfory is being printed, where the sum is an integer between 1 and 57. If `x` is 0 and `y` is greater than 0, the ceiling of half of the value of `y` is being printed. If `x` is greater than 0 and `y` is 0, the ceiling of x divided by 15 is being printed. Otherwise, 0 is being printed.

#Overall this is what the function does:This function takes two integers x and y as input, where x and y are between 0 and 99. It then performs different calculations based on the values of x and y. If both x and y are greater than 0, it calculates the sum of the ceiling of y divided by 2 and the ceiling of x divided by 15, and prints the result. If x is 0 and y is greater than 0, it prints the ceiling of y divided by 2. If x is greater than 0 and y is 0, it prints the ceiling of x divided by 15. If both x and y are 0, it prints 0. The function returns the calculated value as an integer between 1 and 57, or 0 if both x and y are 0.

#State of the program right berfore the function call: stdin contains one input: an integer (t) that is greater than or equal to 1 and less than or equal to 10^4.
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `_` is `t-1`, `t` is an integer greater than or equal to 1 and less than or equal to 10^4, and the function `func_2()` has been called and executed `t` times, but its return value is unknown.

#Overall this is what the function does:Reads an integer from standard input and calls the function `func_2()` that many times.

