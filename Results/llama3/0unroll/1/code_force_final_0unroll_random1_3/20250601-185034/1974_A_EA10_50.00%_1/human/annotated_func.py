#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 10^4), and the rest t inputs are two space-separated integers x and y (0 <= x, y <= 99).
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: The loop will print 'a' number of lines, each containing a single integer. The value of 'a' will be unchanged, and the values of 'x' and 'y' will be the last values read from stdin.

#Overall this is what the function does:Reads a series of inputs from stdin, where the first input is an integer 't' representing the number of subsequent inputs, and each subsequent input is a pair of integers 'x' and 'y'. For each pair, calculates and prints an integer 'z' based on 'x' and 'y', without modifying the original values of 'x' and 'y'. The function prints 't' number of lines, each containing a single integer 'z', and leaves the original values of 'x' and 'y' unchanged.

