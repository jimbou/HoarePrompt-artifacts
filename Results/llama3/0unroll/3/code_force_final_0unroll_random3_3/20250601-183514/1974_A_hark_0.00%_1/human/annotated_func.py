#State of the program right berfore the function call: a and b are non-negative integers.
    return a if a < b else b
    #The program returns the smaller of the two non-negative integers, a and b.

#Overall this is what the function does:This function compares two non-negative integers, a and b, and returns the smaller of the two. It does not modify the input variables. The function's purpose is to determine and return the minimum value between the two input integers.

#State of the program right berfore the function call: stdin contains two inputs: two space-separated integers x and y such that 0 <= x <= 99 and 0 <= y <= 99.
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: an integer between 1 and 89 (which is the sum of bxsfory1 and bxsfory)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: the ceiling of the division of y by 2 (where y is an integer between 0 and 99 and is currently greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: the ceiling of the division of x by 15 (where x is an integer between 1 and 99)
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are integers between 0 and 99, stdin contains no input. Either `x` is 0 or `y` is 0 or both `x` and `y` are 0. It is not the case that `x` is 0 and `y` is greater than 0. If `x` is greater than 0 and `y` is 0, the ceiling of `x` divided by 15 is printed. Otherwise, the number 0 is printed.
        #State: *`x` and `y` are integers between 0 and 99, stdin contains no input. Either `x` is 0 or `y` is 0 or both `x` and `y` are 0. If `x` is 0 and `y` is greater than 0, the ceiling of `y` divided by 2 is printed. If `x` is greater than 0 and `y` is 0, the ceiling of `x` divided by 15 is printed. Otherwise, the number 0 is printed.
    #State: *`x` and `y` are integers between 0 and 99, stdin contains no input. If both `x` and `y` are greater than 0, then `x` is an integer between -1484 and 583, `y` is an integer between 1 and 99, bxsfory is an integer between 1 and 50, bxsfory1 is an integer between 0 and 39, and the sum of bxsfory1 and bxsfory is being printed. If either `x` is 0 or `y` is 0 or both `x` and `y` are 0, then either the ceiling of `y` divided by 2 is printed if `x` is 0 and `y` is greater than 0, the ceiling of `x` divided by 15 is printed if `x` is greater than 0 and `y` is 0, or the number 0 is printed if both `x` and `y` are 0.

#Overall this is what the function does:This function takes two space-separated integers x and y as input from stdin, where 0 <= x <= 99 and 0 <= y <= 99. It then performs calculations based on the values of x and y, and prints an integer value. If both x and y are greater than 0, it calculates and prints the sum of two values: the ceiling of y divided by 2, and the ceiling of x divided by 15 plus 1, after adjusting x based on y. If either x is 0 or y is 0, it prints the ceiling of the non-zero value divided by 2 or 15, respectively. If both x and y are 0, it prints 0. The function does not return any value, but rather prints the calculated result directly.

#State of the program right berfore the function call: stdin contains one input: an integer (t) representing the number of test cases.
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: Output State: `t` is an integer representing the number of test cases, stdin contains no input, and `func_2` has been executed `t` times.

#Overall this is what the function does:Executes a specified number of test cases by reading an integer from standard input and running the `func_2` function that many times, leaving the standard input empty after execution.

