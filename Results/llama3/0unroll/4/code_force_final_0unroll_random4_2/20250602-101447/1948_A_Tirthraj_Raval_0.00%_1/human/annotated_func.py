#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 50 inclusive) and then a series of integers (between 1 and 50 inclusive).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: Output State: The output state after the loop executes all the iterations will be a series of strings, where each string is either 'YES' or 'NO', followed by a pattern of 'A's and 'B's if the corresponding input number is even. The number of strings will be equal to the initial value of `t`. The state of `t` will remain unchanged.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer specifies the number of subsequent integers to process. For each subsequent integer, if it is even, the function prints 'YES' followed by a specific pattern of 'A's and 'B's; if the integer is odd, it prints 'NO'. The function processes all specified integers and outputs the corresponding results, leaving the initial input count unchanged.

