#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase consists of four lines, each line containing two integers x_i, y_i (-1000 <= x_i, y_i <= 1000) representing the coordinates of the corners of a square.
    t = int(input())
    for _ in range(t):
        a = [[int(x) for x in input().split()] for i in range(4)]
        
        x = [p[0] for p in a]
        
        dx = max(x) - min(x)
        
        print(dx * dx)
        
    #State: The output will be the square of the difference between the maximum and minimum x-coordinates of the corners of each square, for each of the t testcases. The value of t will remain unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases. For each test case, it reads four pairs of integers representing the coordinates of the corners of a square. It then calculates and prints the square of the difference between the maximum and minimum x-coordinates of the corners of each square. The function does not modify the input value of t.

