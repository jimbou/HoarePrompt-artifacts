#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n.
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: t = 0, stdin is empty, n, x, y, and arr are undefined.
    #State: *stdin contains multiple test cases. Each test case consists of two lines. The first line contains three integers: n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), y = 0). The second line contains x distinct integers from 1 to n. If the program is run as the main module, then t = 0, stdin is empty, n, x, y, and arr are undefined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, and the second line contains x distinct integers from 1 to n. For each test case, it prints the value of x minus 2. After processing all test cases, the function leaves the standard input empty and the variables n, x, y, and arr undefined.

