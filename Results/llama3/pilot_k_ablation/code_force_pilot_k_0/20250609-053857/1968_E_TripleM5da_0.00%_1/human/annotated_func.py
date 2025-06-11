#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing a single integer n (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: stdin contains no input, stdout contains t*(n+1) lines, each containing two space-separated integers. The first two lines of each iteration are "1 1" and "1 2", and the remaining lines are of the form "i i" where i ranges from 3 to n+1.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the number of lines to print for that test case. The function then prints a series of lines to standard output, where each test case consists of t*(n+1) lines. The first two lines of each test case are always "1 1" and "1 2", followed by n-1 lines of the form "i i", where i ranges from 3 to n+1. The function does not return any value, but instead modifies the standard output.

