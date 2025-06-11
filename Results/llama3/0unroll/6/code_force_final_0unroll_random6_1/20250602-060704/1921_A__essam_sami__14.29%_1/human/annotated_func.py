#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t test cases. Each test case contains four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square with positive area and sides parallel to the coordinate axes.
    t = int(input())
    for steps in range(t):
        a, b = map(int, input().split())
        
        c, d = map(int, input().split())
        
        e, f = map(int, input().split())
        
        g, h = map(int, input().split())
        
        n = (a - e) * (a - e) + (b - f) * (b - f)
        
        x = (c - g) * (c - g) + (d - h) * (d - h)
        
        if x > n:
            print(n)
        else:
            print(x)
        
    #State: The output state will contain t lines, each line containing the minimum of the squared Euclidean distances between points (a, b) and (e, f), and points (c, d) and (g, h) for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four pairs of coordinates representing the corners of a square. It calculates the squared Euclidean distances between two pairs of points for each test case and prints the minimum of these distances. The function processes multiple test cases and outputs the minimum distance for each case, resulting in a series of minimum distances as output.

