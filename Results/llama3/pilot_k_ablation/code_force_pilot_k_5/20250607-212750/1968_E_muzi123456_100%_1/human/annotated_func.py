#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) and then t integers (n_1, n_2, ..., n_t) where 2 <= n_i <= 10^3 for i = 1, 2, ..., t.
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        print(n, end=' ')
        
        print(n)
        
        print(n, end=' ')
        
        print(n - 1)
        
        if n == 3:
            print(2, end=' ')
            print(1)
        else:
            for i in range(1, n - 1):
                print(i, end=' ')
                print(i)
        
        print(' ')
        
    #State: t is equal to 0, n is an integer and is equal to the last input integer, stdin is empty, and the values of n, n, n, n - 1, and the values of i from 1 to n - 1 (if n is greater than 3) or 2 and 1 (if n is equal to 3) are printed, followed by a space.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer (t) represents the number of subsequent integers to process. For each subsequent integer (n), it prints a sequence of numbers: n, n, n, n-1, and then either the numbers 2 and 1 (if n is 3) or the numbers from 1 to n-1 (if n is greater than 3). The function continues this process until all integers have been processed (i.e., until t reaches 0), at which point standard input is empty.

