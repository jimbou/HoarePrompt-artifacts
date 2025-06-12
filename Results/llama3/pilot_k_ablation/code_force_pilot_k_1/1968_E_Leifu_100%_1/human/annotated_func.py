#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing a single integer n (2 <= n <= 10^3).
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        elif n >= 4:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: `t` is an integer between 1 and 50 inclusive, `i` is `t`, stdin is empty, and '1 1', '1 2' have been printed `t` times. For each `n` from 2 to 10^3, if `n` is 3, '2 3' has been printed. If `n` is 4 or more, '2 4' has been printed, and all numbers from 4 to `n` are printed along with themselves.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers, and each subsequent integer n is between 2 and 10^3. For each n, the function prints a series of pairs of numbers, starting with '1 1' and '1 2', and then either '2 3' if n is 3, or '2 4' followed by pairs of numbers from 4 to n if n is 4 or more. The function consumes all input from standard input and produces a specific output pattern based on the input values.

