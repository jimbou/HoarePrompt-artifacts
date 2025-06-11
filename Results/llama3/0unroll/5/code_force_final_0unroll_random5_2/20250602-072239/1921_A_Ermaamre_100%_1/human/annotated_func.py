#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by t test cases. Each test case consists of four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), representing the coordinates of the corners of a square.
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The loop has executed t times, and for each test case, it has printed the square of the difference between the maximum and minimum x-coordinates of the corners of the square. The value of t remains unchanged, and the stdin is empty after reading all the test cases.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of four pairs of integers representing the coordinates of a square's corners, and prints the square of the difference between the maximum and minimum x-coordinates of each square's corners.

