#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 1000) and then a binary string of the same length as the integer.
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
            elif s.count('11') == 1 and count_1 == 2:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: t is 0, n is an integer, s is a binary string of length 0, stdin contains no test cases.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer and a binary string of the same length. It checks if the binary string can be rearranged to form a valid sequence, printing 'YES' if possible and 'NO' otherwise. The function continues processing test cases until all inputs have been consumed, leaving the standard input empty.

