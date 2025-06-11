#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (2 <= n <= 10^3).
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
        
    #State: `t` is an integer between 1 and 50 inclusive, `i` is `t`, `n` is an integer, stdin contains no input, '1 1' has been printed `t` times, '1 2' has been printed `t` times. If `n` is 3, then '2 3' is printed `t` times. If `n` is greater than or equal to 4, then '2 4' is printed `t` times, and the numbers from 4 to `n` (inclusive) are printed with their corresponding numbers `t` times.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the size of a sequence. For each test case, the function prints a sequence of pairs of numbers, starting with '1 1' and '1 2', followed by either '2 3' if n is 3, or '2 4' and the numbers from 4 to n (inclusive) paired with their corresponding numbers if n is greater than or equal to 4. The function repeats this process t times, consuming all input from standard input.

