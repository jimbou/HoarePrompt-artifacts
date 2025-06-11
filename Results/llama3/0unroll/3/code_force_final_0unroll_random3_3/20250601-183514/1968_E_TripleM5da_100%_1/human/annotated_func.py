#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing a single integer n (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: The output state contains 2t+2 lines. The first two lines are "1 1" and "1 2". The remaining 2t lines are of the form "i i" where i ranges from 3 to n for each of the t test cases.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n. For each test case, it prints a specific pattern of numbers to standard output, starting with "1 1" and "1 2", followed by "i i" for i ranging from 3 to n. The function processes multiple test cases and produces a total of 2t + 2 lines of output, where t is the number of test cases.

