#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, c (0 <= a, b, c <= 10^9).
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, c (0 <= a, b, c <= 10^9), p is the last a, q is the last b + c, r is the last c, and the output contains t lines, each containing either (a - (b+c)//3, -1) if c is greater than or equal to (b+c)%3, or -1 if c is less than (b+c)%3 for each line of input.

#Overall this is what the function does:The function reads input from stdin, processes it line by line, and prints output. It accepts an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, c (0 <= a, b, c <= 10^9). For each line, it calculates the value of (a - (b+c)//3, -1) if c is greater than or equal to (b+c)%3, or -1 if c is less than (b+c)%3, and prints the result. The function does not return any value, but instead, prints the output directly.

