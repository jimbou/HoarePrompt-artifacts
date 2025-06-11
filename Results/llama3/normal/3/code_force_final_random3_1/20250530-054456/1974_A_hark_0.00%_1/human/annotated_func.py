#State of the program right berfore the function call: a and b are integers.
    return a if a < b else b
    #The program returns the smaller integer between a and b.

#Overall this is what the function does:This function compares two integers, a and b, and returns the smaller of the two. It takes two integer parameters and returns a single integer value, which is the minimum of the input values.

#State of the program right berfore the function call: stdin contains one input: two space-separated integers x and y such that 0 <= x <= 99 and 0 <= y <= 99.
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: bxsfory1 + bxsfory (where bxsfory1 and bxsfory are integers)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: The ceiling of y/2 (where y is an integer between 0 and 99 and is currently greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: the ceiling of the division of x by 15 (where x is an integer between 1 and 99)
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are integers between 0 and 99, stdin is empty. Either `x` is 0 or `y` is 0 or both `x` and `y` are 0. Additionally, it is not the case that `x` is 0 and `y` is greater than 0. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.
        #State: *`x` and `y` are integers between 0 and 99, stdin is empty. Either `x` is 0 or `y` is 0 or both `x` and `y` are 0. If `x` is 0 and `y` is greater than 0, the ceiling of half of `y` is printed. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.
    #State: `x` and `y` are integers between 0 and 99, stdin is empty. If both `x` and `y` are greater than 0, the sum of bxsfory1 and bxsfory is printed. If either `x` is 0 or `y` is 0 or both `x` and `y` are 0, then either the ceiling of half of `y` is printed if `x` is 0 and `y` is greater than 0, the ceiling of the division of `x` by 15 is printed if `x` is greater than 0 and `y` is 0, or 0 is printed if both `x` and `y` are 0.

#Overall this is what the function does:This function reads two space-separated integers x and y from standard input, where 0 <= x <= 99 and 0 <= y <= 99. It then performs calculations based on the values of x and y and prints the result. If both x and y are greater than 0, it calculates and prints the sum of two values: bxsfory (the ceiling of y/2) and bxsfory1 (the ceiling of x/15 plus 1, or 0 if x is less than or equal to 0). If either x is 0 or y is 0 (or both), it prints the ceiling of y/2 if x is 0 and y is greater than 0, the ceiling of x/15 if x is greater than 0 and y is 0, or 0 if both x and y are 0.

#State of the program right berfore the function call: stdin contains one input: an integer (t) that represents the number of test cases.
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: `t` is an integer representing the number of test cases that must be greater than 0, stdin is empty, _ is `t-1`, and a value has been returned from the function `func_2()`

#Overall this is what the function does:Reads an integer from standard input representing the number of test cases, then calls another function (`func_2`) for each test case, effectively executing it a specified number of times based on the input value.

