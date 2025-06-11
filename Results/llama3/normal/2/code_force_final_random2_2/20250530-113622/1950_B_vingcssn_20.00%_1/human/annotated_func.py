#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 20) followed by t lines each containing an integer n (1 <= n <= 20).
    casos = int(input())
    for c in range(0, casos):
        n = int(input())
        
        if n == 1:
            print('##')
            print('##')
        elif n == 2:
            print('##..')
            print('##..')
            print('..##')
            print('..##')
        elif n == 3:
            print('##..##')
            print('##..##')
            print('..##..')
            print('..##..')
            print('##..##')
            print('##..##')
        elif n == 4:
            print('##..##..')
            print('##..##..')
            print('..##..##')
            print('..##..##')
            print('##..##..')
            print('##..##..')
            print('..##..##')
            print('..##..##')
        else:
            print('No esta en el rango')
        
    #State: `casos` is at least 20, `c` is 19, `n` is an integer, stdin contains no input. If `n` is 1, '##' is printed. If `n` is 2, the strings '##..' and '..##' are printed twice. If `n` is 3, the strings '##..##', '##..##', '..##..', '..##..', '##..##', and '##..##' are printed. If `n` is 4, the strings '##..##..', '##..##..', '..##..##', '..##..##', '##..##..', '##..##..', '##..##..', '..##..##', and '..##..##' are printed. Otherwise, the string 'No esta en el rango' is printed.

#Overall this is what the function does:This function reads a series of integers from standard input and prints a specific pattern of '#' and '.' characters for each integer. The pattern depends on the value of the integer: if the integer is 1, it prints '##' twice; if the integer is 2, it prints '##..' and '..##' twice; if the integer is 3, it prints '##..##', '##..##', '..##..', '..##..', '##..##', and '##..##'; if the integer is 4, it prints '##..##..', '##..##..', '..##..##', '..##..##', '##..##..', '##..##..', '##..##..', '..##..##', and '..##..##'. If the integer is not in the range 1-4, it prints 'No esta en el rango'. The function continues this process until it has read and processed all integers from standard input.

