#State of the program right berfore the function call: stdin contains one input: a positive integer (greater than or equal to 1).
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
        
    #State: Output State: `t` is a positive integer (greater than or equal to 1), stdin contains no input.

#Overall this is what the function does:The function reads a positive integer `t` from standard input, then for each of `t` iterations, it reads another positive integer `n` and prints a series of pairs of numbers. The pairs are always '1 1' and '1 2', followed by either '2 3' if `n` is 3, or '2 4' and then consecutive pairs from '4 4' to `n` `n` if `n` is greater than 3. After processing all iterations, the function leaves the standard input empty.

