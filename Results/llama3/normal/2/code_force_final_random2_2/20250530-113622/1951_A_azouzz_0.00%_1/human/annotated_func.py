#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer and less than or equal to 50.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2 and (cnt1 % 2 == 1 or cnt1 == 1):
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: t is 0, stdin is empty, n is an integer equal to the integer just accepted from stdin, s is a binary string equal to the binary string just accepted from stdin, cnt1 is the number of '1' in s, _ is t. If cnt1 is greater than 2 and cnt1 is even, 'YES' is printed. If cnt1 is greater than 2 and cnt1 is odd or cnt1 equals 1, 'NO' is printed. If cnt1 is not greater than 2 and cnt1 is even and not equal to 1, then if '11' is in s, 'NO' is printed, otherwise 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a binary string (s) of the same length. It then checks the number of '1's in the binary string and prints 'YES' or 'NO' based on the following conditions: if the number of '1's is greater than 2 and even, it prints 'YES'; if the number of '1's is greater than 2 and odd, or if it's 1, it prints 'NO'; if the number of '1's is not greater than 2 and even (but not 1), it checks if the binary string contains '11' and prints 'NO' if it does, otherwise it prints 'YES'. The function processes all test cases and empties the standard input.

