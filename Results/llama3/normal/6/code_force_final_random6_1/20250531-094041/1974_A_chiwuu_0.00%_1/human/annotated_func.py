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
        
    #State: `n` is greater than or equal to 0, `i` is equal to `n`, `a` is an integer equal to the first integer from the input, `b` is an integer equal to the second integer from the input. If `t1` is greater than or equal to `a`, then `t` is an integer equal to twice the value of `b` divided by 5 if twice the value of `b` is divisible by 5, otherwise `t` is an integer equal to twice the value of `b` divided by 5 plus 1, and `t1` is an integer equal to 15 times `t` minus 4 times `b`. If `t1` is less than `a`, then if `t2` is divisible by 15, `t` is an integer equal to twice the value of `b` divided by 5 if twice the value of `b` is divisible by 5, otherwise `t` is an integer equal to twice the value of `b` divided by 5 plus 1 plus `t2` divided by 15, and `t1` is an integer equal to 15 times `t` minus 4 times `b`, and `t2` is an integer equal to `a` minus 15 times `t` plus 4 times `b`. If `t2` is not divisible by 15, then `t` is an integer equal to `t1` divided by 15 plus 1, and `t1` is an integer equal to 15 times `t` minus 4 times `b`, and `t2` is an integer equal to `a` minus 15 times `t` plus 4 times `b`, and the value of `t` is being printed

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates a value based on the second integer of each pair, and prints the calculated value. The calculation involves dividing the second integer by 5, rounding up if necessary, and then adjusting the result based on the first integer of the pair. The function repeats this process for each pair of integers in the input, printing the calculated value for each pair.

