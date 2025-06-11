#State of the program right berfore the function call: stdin contains one input: a positive integer.
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: t is 0, i is n, n is an integer, '1' is printed n times, and the value of i which is n is printed n times, and a space is printed.

#Overall this is what the function does:This function reads a positive integer from standard input, then repeatedly reads another positive integer n and prints '1' and the numbers from 1 to n, each on a new line, until the initial count is exhausted.

