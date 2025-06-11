#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 10^4) and the rest t inputs are two space-separated integers x and y (0 <= x, y <= 99).
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b * 2
        
        if t % 5 == 0:
            t = t // 5
        else:
            t = t // 5 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: The output state will be a list of n integers, each representing the calculated value of t for the corresponding input pair (x, y). The value of n remains unchanged, and the stdin will be empty after the loop finishes executing.

#Overall this is what the function does:This function reads a series of input pairs (x, y) from stdin, calculates a value t based on the given formula, and prints the calculated t values. The function takes no explicit parameters and returns no values, instead, it prints the results directly to the console. The stdin is emptied after the function concludes, and the calculated t values are output as a list of integers, each corresponding to an input pair (x, y).

