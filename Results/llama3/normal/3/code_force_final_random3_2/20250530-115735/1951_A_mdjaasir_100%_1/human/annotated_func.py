#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 ≤ t ≤ 1000) and then a binary string of size t.
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
        
    #State: t is an integer between 0 and 1000, i is t-1, n is an integer equal to the input value, a is a binary string of size t, count is an integer equal to the number of '1' in a, stdin contains no test cases. If count is 0, 'YES' is printed. If count > 2 and count is even, 'YES' is printed. If count is 2 and the second '1' in a is not followed by another '1', 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer t and a binary string of size t. It then checks the number of '1's in the binary string and prints 'YES' or 'NO' based on the following conditions: if there are no '1's, if there are more than two '1's and the count is even, or if there are exactly two '1's and the second '1' is not followed by another '1'. Otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results.

