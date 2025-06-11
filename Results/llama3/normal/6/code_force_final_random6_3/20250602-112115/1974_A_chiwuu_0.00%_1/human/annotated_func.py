#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 99).
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
        
    #State: n is an integer between 0 and 10^4 (inclusive), stdin is empty, i is equal to n, a is an integer between 0 and 99, b is an integer between 0 and 99, t1 is either 11 * (b // 5 + 1) - 4 * b or 15 * t - 4 * b, and t is either 11 * (b // 5 + 1) - 4 * b, 15 * t - 4 * b, t + (a - (11 * (b // 5 + 1) - 4 * b)) // 15, or t + (a - (15 * t - 4 * b)) // 15 + 1.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates a value based on the second integer in each pair, and then adjusts this value based on the first integer in the pair if necessary. It prints the final calculated value for each pair. The function processes a number of pairs specified by an initial integer read from standard input, leaving the input stream empty after processing.

