#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (2 <= n <= 10^3).
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
        
    #State: t is 0, n is an integer between 2 and 10^3 (inclusive)

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the size of a sequence to be printed. For each test case, the function prints a sequence of numbers in a specific pattern, starting with n, then n, then n-1, and finally a sequence of numbers from 1 to n-1, with each number repeated twice. If n is 3, the function prints 2 and 1 instead of the sequence. The function continues this process until all test cases have been processed, at which point the input variables t and n are left in a state where t is 0 and n is an integer between 2 and 10^3 (inclusive).

