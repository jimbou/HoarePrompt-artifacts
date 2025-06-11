#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 20) and then t lines each containing an integer n (1 <= n <= 20).
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
        
    #State: `casos` is an integer between 1 and 20 (inclusive), `c` is `casos - 1`, `n` is an integer between 1 and 20 (inclusive), stdin is empty. If `n` is 1, '##' is printed. If `n` is 2, '##..' is printed, '..##' is printed, and '..##' is printed. If `n` is 3, '##..##' is printed, '..##..' is printed, '..##..' is printed, '##..##' is printed, and '##..##' is printed. If `n` is 4, '##..##..' is printed eight times. If `n` is larger than 4, 'No esta en el rango' is printed.

#Overall this is what the function does:This function reads a number of test cases (between 1 and 20) from standard input, then for each test case, it reads an integer (between 1 and 20) and prints a specific pattern of '#' and '.' characters based on the integer value. If the integer is 1, it prints '##' twice. If the integer is 2, it prints '##..' and '..##' twice. If the integer is 3, it prints '##..##', '..##..', and '##..##' twice. If the integer is 4, it prints '##..##..' eight times. If the integer is larger than 4, it prints 'No esta en el rango'.

