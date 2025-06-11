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
        
    #State: The loop will print n lines, each containing a single integer. The integer on each line is the minimum number of operations required to transform the number y into a number that is greater than or equal to x, where each operation is either dividing the number by 2 (if it is even) or dividing the number by 2 and adding 1 (if it is odd).

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates the minimum number of operations required to transform the second integer into a number greater than or equal to the first integer, and prints the result for each pair. The operations allowed are dividing the number by 2 if it is even, or dividing by 2 and adding 1 if it is odd. The function processes a specified number of pairs, as indicated by the first integer read from standard input.

