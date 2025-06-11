#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t testcases. Each testcase contains four lines, each line contains two integers x_i, y_i (-1000 <= x_i, y_i <= 1000), coordinates of the corners of the square.
    a = int(input())
    for i in range(a):
        x1, y1 = map(int, input().split())
        
        x2, y2 = map(int, input().split())
        
        x3, y3 = map(int, input().split())
        
        x4, y4 = map(int, input().split())
        
        if x1 == x3 and x2 == x4:
            if y1 < y3:
                res = abs(y3 - y1)
            else:
                res = abs(y1 - y3)
        elif x1 == x2 and x3 == x4:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        elif x1 == x4 and x3 == x2:
            if y1 < y2:
                res = abs(y2 - y1)
            else:
                res = abs(y1 - y2)
        
        print(res ** 2)
        
    #State: The loop will execute 'a' number of times, where 'a' is an integer between 1 and 100. In each iteration, it will read four lines of input from stdin, each containing two integers. It will then calculate the side length of a square using the coordinates of its corners and print the square of this side length. The output will be 'a' number of lines, each containing a single integer, which is the square of the side length of the corresponding square. The value of 'a' remains unchanged.

#Overall this is what the function does:This function reads an integer 'a' from standard input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers representing the coordinates of the corners of a square. It calculates the side length of the square using these coordinates and prints the square of this side length. The function repeats this process 'a' times, where 'a' is an integer between 1 and 100. The output is 'a' number of lines, each containing a single integer, which is the square of the side length of the corresponding square.

