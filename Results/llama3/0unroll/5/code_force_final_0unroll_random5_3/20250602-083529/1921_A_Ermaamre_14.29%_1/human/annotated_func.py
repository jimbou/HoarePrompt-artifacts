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
        
    #State: The loop will execute 'a' number of times, each time taking four lines of input from stdin, calculating the area of a square based on the coordinates of its corners, and printing the result. After all iterations, the loop will terminate, and the program will continue executing any remaining code. The value of 'a' will remain unchanged, and stdin will be empty if 'a' is equal to the number of test cases.

#Overall this is what the function does:The function reads an integer 't' from standard input, representing the number of test cases. For each test case, it reads four lines of input, each containing two integers representing the coordinates of the corners of a square. It calculates the area of the square based on the coordinates and prints the result. The function repeats this process 't' times, then terminates, leaving the input stream empty if all test cases are processed.

