#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing a single integer n (2 <= n <= 10^3).
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: The output state will be a series of lines, each containing the number 1 followed by a space and then a number from 1 to n, where n is the input number. The number of lines will be equal to the initial value of t.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the number of lines to print for that test case. The function then prints a series of lines, each containing the number 1 followed by a space and then a number from 1 to n, for each test case. The total number of lines printed is equal to the initial value of t.

