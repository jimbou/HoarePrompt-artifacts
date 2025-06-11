#State of the program right berfore the function call: stdin contains one input: a positive integer.
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        for i in range(1, n + 1):
            print('1', end=' ')
            print(i)
        
        print(' ')
        
    #State: t is 0, stdin is empty, and the output is a series of numbers from 1 to n, where n is the input provided by the user, followed by a space.

#Overall this is what the function does:The function reads a positive integer t from standard input, then reads t positive integers n from standard input. For each n, it prints a series of numbers from 1 to n, with each number followed by a space. After processing all inputs, the function leaves the standard input empty and the standard output containing the printed series of numbers.

