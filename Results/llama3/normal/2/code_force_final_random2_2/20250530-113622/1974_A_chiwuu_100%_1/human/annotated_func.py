#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4), then t pairs of integers x and y (0 <= x, y <= 99).
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
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
        
    #State: `n` is greater than or equal to 0, `i` is equal to `n`, `a` is an integer between 0 and 99, `b` is an integer between 0 and 99, `t1` is an integer between -396 and 750, stdin is empty. If `t1` is greater than or equal to `a`, `t` is an integer between 0 and 50. If `t1` is less than `a`, then if `t2` is a multiple of 15, `t` is an integer between 0 and 50 if `t` is even, otherwise `t` is an integer between 1 and 50. Otherwise, `t` is an integer between 1 and 100.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, applies a transformation to the second integer of each pair based on its parity, and then adjusts the result based on the difference between the first integer and the transformed second integer. The function prints the adjusted result for each pair. The function processes all input pairs and leaves the standard input empty.

