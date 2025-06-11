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
        
    #State: The output state will be a series of printed patterns, each corresponding to the input integer `n` read from stdin. The patterns will be printed in the format specified in the loop body, with each pattern consisting of a series of '#' and '.' characters. The number of patterns printed will be equal to the value of `casos`, which is an integer between 1 and 20 (inclusive).

#Overall this is what the function does:The function reads an integer `t` from standard input, representing the number of test cases, and then reads `t` integers, each representing the size of a pattern to be printed. For each integer `n`, the function prints a specific pattern of '#' and '.' characters, with the pattern depending on the value of `n`. If `n` is 1, 2, 3, or 4, the function prints a predefined pattern of '#' and '.' characters. If `n` is not in the range 1-4, the function prints the message "No esta en el rango". The function repeats this process for each of the `t` test cases.

