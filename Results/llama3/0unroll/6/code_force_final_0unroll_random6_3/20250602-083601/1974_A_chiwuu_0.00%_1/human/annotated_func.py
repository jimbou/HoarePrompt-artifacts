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
        
    #State: The loop will print n lines, each containing an integer. The integer on each line represents the minimum number of operations required to transform the given pair of integers (x, y) into a pair (a, b) such that a >= b * 4 and a <= b * 15. The value of n and the input pairs (x, y) remain unchanged.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, calculates the minimum number of operations required to transform each pair into a new pair where the first integer is between 4 and 15 times the second integer, and prints the result for each pair. The function does not modify the input values.

