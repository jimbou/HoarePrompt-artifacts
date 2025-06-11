#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer (2 <= n <= 2 * 10^5 and n is even), then two strings of length n consisting of '<' and '>' characters. The sum of n over all test cases doesn't exceed 2 * 10^5.
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
        
    #State: i is equal to the number of test cases, n is an integer equal to the input value, a is a string equal to the first input string, b is a string equal to the second input string, stdin is empty. If b[-2] is not '>', 'NO' is printed for each test case where this condition is true. If b[-2] is '>', then if n is 1, 'YES' is printed for each test case where this condition is true. If n is not 1, then the values of k which are all odd numbers from 1 to n - 1 have been printed for each test case where this condition is true, and if no_path is True, 'YES' is printed for each test case where this condition is true, otherwise 'NO' is printed for each test case where this condition is true.

#Overall this is what the function does:This function processes multiple test cases from standard input. Each test case consists of an even integer n and two strings a and b of length n, containing '<' and '>' characters. The function checks if a path exists between the strings based on certain conditions. If the second last character of string b is not '>', it prints 'NO' for that test case. If n is 1, it prints 'YES'. Otherwise, it checks if all characters at even indices in string b are '>' and all characters at odd indices in string a are '>'. If both conditions are true, it prints 'YES', otherwise 'NO'. Additionally, for test cases where n is not 1 and the second last character of string b is '>', it prints the odd indices from 1 to n-1. The function processes all test cases and then terminates, leaving the standard input empty.

