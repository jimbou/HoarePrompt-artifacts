#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers x and y (0 <= x, y <= 99).
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
        
    #State: Output State: The output state will be a list of `n` integers, each representing the calculated value of `t` for the corresponding input pair `(x, y)`.

#Overall this is what the function does:This function reads a series of input pairs (x, y) from standard input, calculates a value t based on the given formula, and prints the calculated value of t for each pair. The function takes no explicit parameters and returns no value, instead, it prints the calculated values to the standard output. The output is a list of integers, each representing the calculated value of t for the corresponding input pair (x, y).

