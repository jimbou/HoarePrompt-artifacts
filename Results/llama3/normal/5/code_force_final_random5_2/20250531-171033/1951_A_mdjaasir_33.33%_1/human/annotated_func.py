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
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: t is a positive integer greater than or equal to 0 and less than or equal to 50, i is t, n is an integer, a is a binary string, count is the number of '1's in a, stdin contains no test cases. If count is 0, 'YES' is printed. If count is greater than 2 and is even, 'YES' is printed. If count is 2 and the first '1' in a is not followed by another '1', 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer and a binary string of the same length. It then checks the number of '1's in the binary string and prints 'YES' or 'NO' based on the following conditions: if there are no '1's, if there are more than two '1's and the count is even, or if there are exactly two '1's and they are not consecutive. Otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results.

