#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing an integer n (3 <= n <= 78).
    cases = int(input())
    for i in range(cases):
        arr = []
        
        lex = int(input())
        
        for j in range(2):
            if lex <= 26:
                arr.append(1)
                lex = lex - 1
            elif lex < 52:
                arr.append(26)
                lex = lex - 26
            else:
                arr.append(26)
                lex = lex - 26
        
        arr.append(lex)
        
        arr.sort()
        
        for k in range(3):
            print(chr(arr[k] + 96), end='')
        
    #State: The output will be a string of 3 characters for each test case, representing the alphabetical representation of the input number. The characters will be in ascending order. For example, if the input is 3, the output will be "abc". If the input is 28, the output will be "abc". If the input is 79, the output will be "xyz".

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of an integer. For each case, it generates a string of three characters representing the alphabetical equivalent of the input number, with the characters in ascending order. The function prints these strings for each test case.

