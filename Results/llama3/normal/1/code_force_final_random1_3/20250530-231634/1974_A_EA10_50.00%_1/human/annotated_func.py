#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4), then t pairs of integers x and y (0 <= x, y <= 99).
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: a is an integer between 0 and 10^4 (inclusive), i is a, x is an integer equal to the last input, y is an integer equal to the last input. If m is less than a, z is an integer equal to (y + 1) // 2 + (x - 15 * ((y + 1) // 2) + y * 4 + 15 - 1) // 15. Otherwise, z is an integer equal to (y + 1) // 2, and the value of z is being printed.

#Overall this is what the function does:This function reads a series of input pairs from the standard input, where the first input is the number of pairs to follow. For each pair of integers x and y, it calculates a value z based on the given formula and prints the result. The calculation of z depends on the intermediate value m; if m is less than the initial input a, z is adjusted accordingly. The function processes all input pairs and outputs the calculated z values.

