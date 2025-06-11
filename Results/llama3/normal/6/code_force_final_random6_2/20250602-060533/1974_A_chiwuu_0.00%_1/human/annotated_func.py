#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t pairs of integers x and y (0 <= x, y <= 99).
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
        
    #State: `n` is greater than or equal to 0, `i` is equal to `n`, `a` is an integer, `b` is an integer, `t1` is an integer. If `t1` is greater than or equal to `a`, then `t1` is equal to 2b * 3 - b * 4 if `t` is divisible by 5, or (2 times the value of b) * 3 // 5 * 15 + 15 - b * 4 if `t` is not divisible by 5. If `t1` is less than `a`, then `t2` is an integer and is equal to `a - t1`. If `t2` is divisible by 15, then `t` is equal to `t + t2 // 15`. Otherwise, `t` is equal to `t + t2 // 15 + 1` and is an integer. After the update of `t`, if `t` is divisible by 5, then `t1` is equal to 2b * 3 - b * 4, which is an integer and divisible by 5. Otherwise, `t1` is equal to (2 times the value of b) * 3 // 5 * 15 + 15 - b * 4 and `t1` is not divisible by 5, and the value of `t` is printed

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates a value based on the second integer of each pair, and prints the calculated value. The calculation involves multiplying the second integer by 2, dividing by 5, and adjusting the result based on whether the division is exact or not. If the calculated value is less than the first integer of the pair, the function further adjusts the result by adding a multiple of 15. The function repeats this process for each pair of integers in the input, printing the final calculated value for each pair.

