#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (between 1 and 1000) and then a binary string of the same length as the integer.
    t = int(input())
    while t > 0:
        n = int(input())
        
        s = input()
        
        if n == 2:
            if s == '00':
                print('YES')
            else:
                print('NO')
        else:
            count_1 = s.count('1')
            if count_1 % 2 != 0:
                print('NO')
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: The loop will finish executing all iterations, and the value of `t` will be 0. The output will be a series of 'YES' or 'NO' for each test case, indicating whether the binary string can be rearranged into a valid binary number. The stdin will be empty after all test cases have been processed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer and a binary string of the same length. It checks if the binary string can be rearranged into a valid binary number and prints 'YES' or 'NO' for each test case accordingly. The function continues processing test cases until all inputs have been consumed, leaving the standard input empty.

