#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t pairs of integers x and y (0 <= x, y <= 99).
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: a is an integer between 1 and 10^4, i is a-1, x is an integer between 0 and 99, y is an integer between 0 and 99, z is an integer between 0 and 50 + (x - m + 14) // 15 if m is less than a, otherwise z is an integer between 0 and 50, m is an integer between -395 and 0, stdin contains 0 pairs of integers x and y (0 <= x, y <= 99).

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates a value based on each pair, and prints the calculated value. The function takes no arguments and returns no value. It consumes all input pairs from standard input, leaving it empty. The calculated value is determined by a formula involving the input integers, and its range depends on the input values.

