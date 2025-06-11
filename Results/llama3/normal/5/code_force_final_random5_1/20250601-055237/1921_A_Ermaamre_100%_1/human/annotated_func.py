#State of the program right berfore the function call: stdin contains one input: an integer t (1 <= t <= 100), followed by 4t lines, each containing two integers x and y (-1000 <= x, y <= 1000), representing the coordinates of the corners of a square.
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: t is an integer between 1 and 100, _ is t-1, a is a 4x2 matrix containing integers, x is a list of 4 integers, dx is an integer equal to the difference between the maximum and minimum values in x, stdin is empty, and the square of dx is being printed.

#Overall this is what the function does:This function reads a series of square coordinates from standard input, calculates the side length of each square, and prints the area of each square. It accepts no parameters and returns no value, instead printing the areas directly. The function processes a variable number of squares, as specified by the initial input, and leaves the standard input empty after processing.

