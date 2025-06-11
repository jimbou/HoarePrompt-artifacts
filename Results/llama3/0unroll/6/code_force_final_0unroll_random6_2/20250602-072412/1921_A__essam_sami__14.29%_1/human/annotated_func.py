#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 100) followed by 4t lines, each containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000).
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
        
    #State: The output will contain t lines, each containing the smaller of the two squared Euclidean distances between the points (a, b) and (e, f), and the points (c, d) and (g, h).

#Overall this is what the function does:Calculates and prints the smaller of the two squared Euclidean distances between two pairs of points for a given number of test cases.

