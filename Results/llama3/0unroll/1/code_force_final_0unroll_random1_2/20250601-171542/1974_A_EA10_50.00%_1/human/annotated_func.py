#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4) and then t pairs of integers x and y (0 <= x, y <= 99).
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: The loop will print a values, each of which is the smallest integer z such that 15z - 4y >= x.

#Overall this is what the function does:This function reads a series of input pairs (x, y) from standard input, where the number of pairs is specified by an initial integer t. For each pair, it calculates and prints the smallest integer z such that 15z - 4y is greater than or equal to x. The function does not return any value but instead prints the calculated z values directly to the standard output.

