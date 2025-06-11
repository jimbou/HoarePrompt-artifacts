#State of the program right berfore the function call: a and b are integers.
    return a if a < b else b
    #The program returns the smaller integer between a and b.

#Overall this is what the function does:This function compares two integers, a and b, and returns the smaller one. It takes two integer parameters, a and b, and returns a single integer value, which is the minimum of the two input integers.

#State of the program right berfore the function call: stdin contains one input: two space-separated integers x and y such that 0 <= x <= 99 and 0 <= y <= 99.
    x, y = map(int, input().split())
    if (x > 0 and y > 0) :
        bxsfory = math.ceil(y / 2)
        x = x - bxsfory * 15 + y * 4
        bxsfory1 = 0 if x <= 0 else math.ceil(x / 15) + 1
        print(bxsfory1 + bxsfory)
        #This is printed: sum of bxsfory1 and bxsfory (where bxsfory1 is an integer between 0 and 26 and bxsfory is an integer between 1 and 50)
    else :
        if (x == 0 and y > 0) :
            print(math.ceil(y / 2))
            #This is printed: the ceiling of the division of y by 2 (where y is an integer between 0 and 99 and is greater than 0)
        else :
            if (x > 0 and y == 0) :
                print(math.ceil(x / 15))
                #This is printed: 1
            else :
                print(0)
                #This is printed: 0
            #State: *`x` and `y` are integers between 0 and 99, stdin is empty. Either `x` is 0 or `y` is 0 or both `x` and `y` are 0. It is not the case that `x` is 0 and `y` is greater than 0. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.
        #State: *`x` and `y` are integers between 0 and 99, stdin is empty. Either `x` is 0 or `y` is 0 or both `x` and `y` are 0. If `x` is 0 and `y` is greater than 0, the smallest integer not less than y/2 is printed. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.
    #State: `x` and `y` are integers between 0 and 99, stdin is empty. If both `x` and `y` are greater than 0, the sum of bxsfory1 and bxsfory is printed, where the sum is an integer between 1 and 76. If `x` is 0 and `y` is greater than 0, the smallest integer not less than y/2 is printed. If `x` is greater than 0 and `y` is 0, the ceiling of the division of `x` by 15 is printed. Otherwise, 0 is printed.

#Overall this is what the function does:The function reads two space-separated integers x and y from standard input, where 0 <= x <= 99 and 0 <= y <= 99. It then performs calculations based on the values of x and y, and prints the result. If both x and y are greater than 0, it calculates the sum of two values, bxsfory and bxsfory1, and prints the sum. If x is 0 and y is greater than 0, it prints the ceiling of y divided by 2. If x is greater than 0 and y is 0, it prints the ceiling of x divided by 15. If both x and y are 0, it prints 0. The function does not return any value, and its purpose is to perform these calculations and print the result based on the input values.

#State of the program right berfore the function call: stdin contains one input: an integer (greater than or equal to 1 and less than or equal to 10^4)
    t = int(input())
    for _ in range(t):
        func_2()
        
    #State: The value of `t` is 0, and the state of `func_2` is unchanged, as it is not affected by the loop head and body. The state of `stdin` remains unchanged, as it contains no input.

#Overall this is what the function does:Reads an integer from standard input, representing the number of times to call `func_2`, and calls `func_2` that many times, without modifying the state of `func_2` or standard input.

