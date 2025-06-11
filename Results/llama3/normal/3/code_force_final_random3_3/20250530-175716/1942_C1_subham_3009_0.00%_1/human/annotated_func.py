#State of the program right berfore the function call: stdin contains t test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y, where 4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), and y = 0. The second line contains x distinct integers from 1 to n.
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: t is 0, n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5), y is an integer, arr is a list of x distinct integers from 1 to n, stdin is empty, and the value of x - 2 is printed for each test case.
    #State: *stdin contains t test cases. If t is 0, n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5), y is an integer, arr is a list of x distinct integers from 1 to n, stdin is empty, and the value of x - 2 is printed for each test case.

#Overall this is what the function does:This function reads test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, where n is between 4 and 10^9, x is between 2 and min(n, 2 * 10^5), and y is 0. The second line contains x distinct integers from 1 to n. For each test case, the function prints the value of x - 2, which is an integer between 0 and min(n, 2 * 10^5) - 2. The function continues reading and processing test cases until there are no more test cases in standard input.

