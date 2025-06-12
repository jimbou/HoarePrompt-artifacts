#State of the program right berfore the function call: stdin contains two inputs: first an integer (t) and then t number of integers (n). Both t and n are positive integers and n is less than or equal to 1000.
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
        
    #State: t is 0, stdin is empty

#Overall this is what the function does:This function reads a positive integer (t) from standard input, followed by t number of positive integers (n), each less than or equal to 1000. It then prints a specific pattern of numbers for each n, including n, n-1, and a sequence of numbers from 1 to n-1, with some variations for n=3. After processing all inputs, the function leaves the standard input empty and the variable t as 0.

