#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines. The first line contains three integers, n, x, and y, where n is the number of sides of the polygon, x is the number of vertices Bessie has chosen, and y is the maximum number of other vertices that can be chosen. The second line contains x distinct integers from 1 to n, representing the vertices Bessie has chosen.
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: t is 0, n is an integer, x is an integer, y is an integer, arr is a list of x distinct integers from 1 to n, stdin is empty, and the value of x - 2 is printed for each test case.
    #State: The program reads input from stdin, processes it, and prints the value of x - 2 for each test case if the program is run as the main module, otherwise, it does nothing.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the value of x - 2 for each test case if the program is run as the main module, otherwise, it does nothing. It accepts no parameters and returns no value. The function's purpose is to calculate and print the value of x - 2 for each test case, where x is the number of vertices Bessie has chosen. The final state of the program after it concludes is that the value of x - 2 is printed for each test case, and stdin is empty.

