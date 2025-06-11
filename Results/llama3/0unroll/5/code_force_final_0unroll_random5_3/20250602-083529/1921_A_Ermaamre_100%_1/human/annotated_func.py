#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by 4t lines, each containing two integers x and y (-1000 <= x, y <= 1000), such that the 4t lines describe the coordinates of the corners of a square with sides parallel to the coordinate axes and positive area.
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The standard output contains t lines, each containing a single integer representing the square of the difference between the maximum and minimum x-coordinates of the four points in each set. The value of t and the contents of stdin remain unchanged.

#Overall this is what the function does:Reads a series of square coordinates from standard input, calculates the square of the difference between the maximum and minimum x-coordinates for each square, and prints the results to standard output, leaving the input unchanged.

