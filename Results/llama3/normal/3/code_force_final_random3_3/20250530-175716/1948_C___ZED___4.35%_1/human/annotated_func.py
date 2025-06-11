#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. n is even.
    for i in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        if b[-2] != '>':
            print('NO')
        elif n == 1:
            print('YES')
        else:
            no_path = True
            for k in range(0, n, 2):
                if b[k] != '>':
                    no_path = False
            if not no_path:
                no_path = True
                for k in range(1, n - 1, 2):
                    print(k)
                    if a[k] != '>':
                        no_path = False
            if no_path:
                print('YES')
            else:
                print('NO')
        
    #State: i is t-1, stdin is empty, n is an integer between 2 and 2 * 10^5 inclusive, a is a string of length n consisting of '<' and '>' characters, b is a string of length n consisting of '<' and '>' characters, no_path is False, k is an integer. If b[-2] is not '>', 'NO' is printed. Otherwise, if n is 1, 'YES' is printed. If n is not 1, then if a[k] is '>' for some k in the range 1 to n-1 with a step of 2, then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by two strings of length n containing '<' and '>' characters. It then checks if a path exists between the two strings based on certain conditions. If the second string does not end with a '>', it prints 'NO'. If the length of the strings is 1, it prints 'YES'. Otherwise, it checks if there is a '>' character at every odd index in the first string. If such a character is found, it prints 'YES'. If not, it prints 'NO'. The function processes all test cases and prints the result for each case.

