#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer less than or equal to 50.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        a = input()
        
        count = a.count('1')
        
        if count == 0:
            print('YES')
        elif count > 2 and count % 2 == 0:
            print('YES')
        elif count == 2:
            if a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: t is 0, i is t, n is a positive integer less than or equal to 50, a is a binary string of the same length as n, count is the number of '1' bits in a, stdin contains no test cases. If count is 0, 'YES' is printed. If count is greater than 2 and is even, 'YES' is printed. If count is 2 and the second '1' bit is not immediately after the first '1' bit, 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a binary string (a) of the same length as n. It then checks the number of '1' bits in the binary string and prints 'YES' if the count is 0, or if the count is greater than 2 and even, or if the count is 2 and the second '1' bit is not immediately after the first '1' bit. Otherwise, it prints 'NO'. The function processes all test cases and then terminates, leaving the standard input empty.

