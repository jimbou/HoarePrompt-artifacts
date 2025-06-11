#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t pairs of integers x and y (0 <= x, y <= 99).
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: a is an integer between 1 and 10^4 (inclusive) and is equal to 0, i is equal to a, stdin is empty, x is an integer between 0 and 99 (inclusive), y is an integer between 0 and 99 (inclusive), m is an integer, z is an integer between 0 and 50 (inclusive) plus the integer division of (x - m + 14) by 15 if m is less than a, otherwise z remains unchanged.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, performs a calculation on each pair, and prints the result. The calculation involves a series of arithmetic operations and conditional adjustments. The function processes all input pairs and produces a corresponding output for each pair, leaving the input stream empty upon completion.

