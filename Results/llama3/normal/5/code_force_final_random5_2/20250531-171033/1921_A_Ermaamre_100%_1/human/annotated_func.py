#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by t testcases. Each testcase contains four lines, each line contains two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of the square.
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: t is an integer between 1 and 100, _ is t-1, a is a 4x4 matrix of integers, x is a list of 4 integers, dx is an integer equal to the difference between the maximum and minimum values in x, and the square of dx is being printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four pairs of integers representing the coordinates of a square's corners. For each test case, it calculates the side length of the square (as the difference between the maximum and minimum x-coordinates) and prints the square of this side length. The function processes a specified number of test cases, which is provided as the first input.

