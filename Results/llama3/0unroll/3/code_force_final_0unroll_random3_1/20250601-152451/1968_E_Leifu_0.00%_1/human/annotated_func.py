#State of the program right berfore the function call: stdin contains one input: a positive integer.
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
        
    #State: Output State: `t` is a positive integer, stdin contains no input, and the output contains `t` sets of lines, each set containing the lines '1 1', '1 2', and either '2 3' if the corresponding input number is 3, or '2 4' followed by lines of the form 'x x' for x ranging from 4 to the input number.

#Overall this is what the function does:This function reads a positive integer `t` from standard input, then for each of `t` iterations, it reads another positive integer `n` and prints a specific pattern of lines based on the value of `n`. If `n` is 3, it prints '1 1', '1 2', and '2 3'. For any other value of `n`, it prints '1 1', '1 2', '2 4', and then a series of lines from '4 4' up to 'n n'. The function continues this process `t` times, consuming all input and producing a structured output without returning any value.

