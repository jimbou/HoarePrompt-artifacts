#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 20) followed by t lines each containing an integer n (1 ≤ n ≤ 20).
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
        
    #State: `casos` is an integer between 1 and 20 and greater than or equal to 0, `c` is equal to `casos`, `n` is an integer between 1 and 20, stdin contains 0 lines each containing an integer n (1 ≤ n ≤ 20). If `n` is 1, '##' is printed. If `n` is 2, '##..' and '..##' are printed. If `n` is 3, '##..##', '..##..', '..##..', '##..##', and '##..##' are printed. If `n` is 4, '##..##..' and '..##..##' are printed eight times. If `n` is not 1, 2, 3, or 4, 'No esta en el rango' is printed.

#Overall this is what the function does:The function reads an integer `t` from standard input, representing the number of test cases. For each test case, it reads an integer `n` and prints a specific pattern of '#' and '.' characters based on the value of `n`. If `n` is 1, it prints two lines of '##'. If `n` is 2, it prints four lines of '##..' and '..##'. If `n` is 3, it prints six lines of '##..##', '..##..', and '##..##'. If `n` is 4, it prints eight lines of '##..##..' and '..##..##'. If `n` is not between 1 and 4, it prints 'No esta en el rango'. The function repeats this process for all `t` test cases.

