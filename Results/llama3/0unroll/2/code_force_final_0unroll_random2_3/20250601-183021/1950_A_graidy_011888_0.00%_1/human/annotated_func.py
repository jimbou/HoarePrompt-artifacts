#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing three digits a, b, c (0 <= a, b, c <= 9).
    i = 1
    while i <= 1000:
        x = randint(1, 9)
        
        y = randint(1, 9)
        
        z = randint(1, 9)
        
        res = ''
        
        if x < y:
            if y > z:
                res = 'peak'
            elif y < z:
                res = 'stair'
            else:
                res = 'none'
        else:
            res = 'none'
        
        print(x, y, z, sep=' ')
        
        print(res)
        
        i += 1
        
    #State: i is 1001, stdin is empty.

#Overall this is what the function does:This function generates 1000 sets of three random digits between 1 and 9, prints each set, and then prints a string indicating whether the digits form a "peak" (the middle digit is greater than the first and last), a "stair" (the middle digit is greater than the first but less than the last), or "none" (otherwise). The function does not take any input and does not return any value.

