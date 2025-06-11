#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n.
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: t is 0, n is an integer between 4 and 10^9 inclusive, x is an integer between 1 and 2 * 10^5 inclusive, y is an integer, arr is a list of x integers, stdin is empty, and the value of x - 2 which is an integer between -1 and 2 * 10^5 - 2 inclusive is being printed.
    #State: *stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n. After the program executes, if the program is run as the main module, the value of x - 2 which is an integer between -1 and 2 * 10^5 - 2 inclusive is being printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) followed by x distinct integers. It then prints the value of x - 2 for each test case. The function does not modify the input values or perform any calculations beyond printing the result. The final state of the program is that the input has been processed, and the results (x - 2) have been printed to the console.

