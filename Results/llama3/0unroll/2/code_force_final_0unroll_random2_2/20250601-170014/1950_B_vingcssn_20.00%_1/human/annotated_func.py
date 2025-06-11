#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 20) followed by t lines, each containing an integer n (1 <= n <= 20).
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
        
    #State: The output state will be a series of printed patterns based on the input integers. For each input integer n, a specific pattern of '#' and '.' characters will be printed. The pattern will have a size of n x n, with '#' characters forming a border around a '.' filled interior. If the input integer is not between 1 and 4 (inclusive), the message 'No esta en el rango' will be printed. The output will be a concatenation of these patterns for each input integer.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the size of a pattern to be printed. For each n, the function prints a pattern of '#' and '.' characters, with '#' forming a border around a '.' filled interior, if n is between 1 and 4 (inclusive). If n is outside this range, it prints the message 'No esta en el rango'. The function repeats this process for each test case, concatenating the output patterns.

