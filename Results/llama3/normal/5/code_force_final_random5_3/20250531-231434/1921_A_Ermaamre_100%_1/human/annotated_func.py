#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase contains four lines, each line contains two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), coordinates of the corners of the square.
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: t is an integer between 1 and 100, _ is t-1, a is a 4x4 matrix of integers, x is a list of 4 integers, dx is an integer equal to the difference between the maximum and minimum values in x, and the square of dx is printed.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers representing the coordinates of the corners of a square. It then calculates the difference between the maximum and minimum x-coordinates (dx) and prints the square of dx. The function repeats this process t times, effectively calculating and printing the area of each square defined by the input coordinates.

