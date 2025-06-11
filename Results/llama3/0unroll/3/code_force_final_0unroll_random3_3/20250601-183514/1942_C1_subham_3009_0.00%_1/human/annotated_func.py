#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y, where 4 <= n <= 10^9, 2 <= x <= min(n, 2*10^5), and y = 0. The second line contains x distinct integers from 1 to n.
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: The output state is the number of test cases minus two, printed for each test case.
    #State: *The program executes the test cases, and for each test case, it prints the number of test cases minus two, unless the program is not run as the main module, in which case nothing is executed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) followed by x distinct integers. It then prints the value of x minus 2 for each test case. The function does not modify the input values or perform any calculations beyond the subtraction. The output is solely dependent on the value of x in each test case.

