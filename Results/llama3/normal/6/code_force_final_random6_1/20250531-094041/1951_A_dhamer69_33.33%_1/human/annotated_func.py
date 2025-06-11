#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer less than or equal to 50.
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
        
    #State: t is 0, n is an integer equal to the first input, s is a binary string of length t equal to the second input, stdin contains no test cases. If n is 2, 'YES' is printed if s is '00', otherwise 'NO' is printed. If n is not 2, 'NO' is printed if the number of '1' in s is odd or if the number of '1' in s is even and s contains exactly one occurrence of '11', otherwise 'YES' is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of a positive integer (n) and a binary string (s) of the same length. It checks the validity of the binary string based on the length and the number of '1's. If the length is 2, it prints 'YES' if the string is '00', otherwise 'NO'. If the length is not 2, it prints 'NO' if the number of '1's is odd or if the number of '1's is even and the string contains exactly one '11', otherwise 'YES'. The function continues processing test cases until all inputs have been read.

