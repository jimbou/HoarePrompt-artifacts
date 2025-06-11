#State of the program right berfore the function call: stdin contains one input: an integer t (1 ≤ t ≤ 50) followed by t lines each containing a single integer n (2 ≤ n ≤ 10^3).
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
        
    #State: t is 0, stdin is empty, and the values of all integers from 1 to 10^3 - 1 are printed twice, and a space is printed.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers to process. For each integer n, it prints the value of n twice, followed by the values from 1 to n-1 (inclusive) printed twice, except for the case where n is 3, in which it prints 2 and 1. After processing all integers, the function leaves the standard input empty and the value of t as 0.

