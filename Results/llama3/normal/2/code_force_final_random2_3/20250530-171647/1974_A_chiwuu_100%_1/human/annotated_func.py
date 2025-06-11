#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 99).
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
        
    #State: n is an integer between 0 and 10^4, i is n-1, a is an integer between 0 and 99, b is an integer between 0 and 99, t1 is an integer, if t is even then t1 is between -396 and 735, if t is odd then t1 is between -395 and 736, t is an integer between 0 and 99, stdin contains 0 lines. If t1 is greater than or equal to a, then t is between 0 and 49 if even, and between 1 and 50 if odd. If t1 is less than a, then t2 is an integer, if t is even then t2 is between -396 and 99, if t is odd then t2 is between -395 and 99. If t2 is a multiple of 15, then t is between 0 and 49 if even, and between 1 and 50 if odd. Otherwise, if t is even then t is between 1 and 25, otherwise t is between 2 and 26, and the value of t is being printed. If t1 is less than a and t2 is not a multiple of 15, then t is increased by 1. If t1 is less than a and t2 is a multiple of 15, then t is increased by t2 divided by 15. The value of t after the increments is being printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates a value based on the second integer in each pair, and prints the calculated value. The calculation involves checking if the second integer is even or odd, performing arithmetic operations, and potentially incrementing the result based on the difference between the calculated value and the first integer in the pair. The function repeats this process for a number of pairs specified by the first integer read from standard input.

