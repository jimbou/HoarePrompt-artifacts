#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (between 1 and 1000) and then a binary string of the same length as the integer.
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
        
    #State: t is an integer between 1 and 1000, i is t-1, n is an integer, a is a binary string of length t, count is the number of '1's in a, stdin contains multiple test cases minus t. If count is 0, 'YES' is printed. If count is greater than 2 and is even, 'YES' is printed. If count is 2 and the first '1' in a is not followed by another '1', 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:The function processes multiple test cases from standard input. Each test case consists of an integer and a binary string of the same length. It counts the number of '1's in the binary string and prints 'YES' if the count is 0, greater than 2 and even, or 2 and the first '1' is not followed by another '1'. Otherwise, it prints 'NO'. The function iterates through all test cases and prints the corresponding results.

