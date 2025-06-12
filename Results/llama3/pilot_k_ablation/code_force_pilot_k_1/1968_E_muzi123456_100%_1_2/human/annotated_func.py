#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) and then t integers (n). The integer t is a positive integer and each n is an integer such that 2 <= n <= 10^3.
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
        
    #State: t is 0, stdin is empty.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer (t) specifies the number of subsequent integers (n) to process. For each n, it prints a sequence of numbers: first n, then n, then n, then n-1, followed by a sequence of numbers from 1 to n-1 (inclusive) where each number is printed twice, except when n is 3, in which case it prints 2 and 1. After processing all integers, the function leaves the standard input empty and the variable t set to 0.

