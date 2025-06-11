#State of the program right berfore the function call: stdin contains one input: an integer (t) (1 <= t <= 50), followed by t inputs: integers (n) (2 <= n <= 10^3).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        else:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: `t` is an integer between 1 and 50 inclusive, `i` is `t-1`, `n` is an integer that has been input from stdin, stdin contains no input, '1 2' has been printed. If `n` is 3, '2 3' is being printed. If `n` is greater than or equal to 4, '2 4' is printed, and for all integers `k` such that 4 <= `k` <= `n`, '`k` `k`' is printed, and '1 1' is printed, and '1 2' is printed, and either '2 3' is printed if `n` is 3 or '2 4' is printed if `n` is greater than or equal to 4, and this pattern of printing '1 1', '1 2', and either '2 3' or '2 4' and '`k` `k`' for `k` from 4 to `n` is repeated `t-1` times.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer (t) represents the number of test cases, and each subsequent integer (n) represents the size of a sequence. For each test case, the function prints a specific pattern of numbers: '1 1', '1 2', and either '2 3' if n is 3 or '2 4' followed by 'k k' for k from 4 to n if n is greater than or equal to 4. This pattern is repeated t times.

