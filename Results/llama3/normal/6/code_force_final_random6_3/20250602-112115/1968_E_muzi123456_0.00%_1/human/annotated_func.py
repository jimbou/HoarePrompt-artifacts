#State of the program right berfore the function call: stdin contains one input: an integer (t) (1 <= t <= 50) representing the number of test cases. For each test case, stdin contains a single integer n (2 <= n <= 10^3).
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: t is 0, n is an integer, i is n, the number 1 is printed n times, the values of i from 1 to n are printed, and a space is printed, and an additional space is printed for each test case in stdin, and stdin contains no input.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a single integer n. For each test case, it prints the number 1 followed by the numbers from 1 to n, separated by spaces, and then prints an additional space. The function continues this process until all test cases have been read and processed, at which point it terminates.

