#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and/or '>'. n is even.
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
        
    #State: The output state will contain t lines, each containing either 'YES' or 'NO'. For each test case, if the last second character of string b is not '>', the output will be 'NO'. If n is 1, the output will be 'YES'. Otherwise, the output will be 'YES' if there is a path from the first character of string a to the last character of string b, and 'NO' otherwise. A path exists if all characters at even indices in string b are '>' and all characters at odd indices in string a are '>'.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and two strings a and b of length n. It then determines whether there exists a path from the first character of string a to the last character of string b based on certain conditions. If the last second character of string b is not '>', it outputs 'NO'. If n is 1, it outputs 'YES'. Otherwise, it checks if all characters at even indices in string b are '>' and all characters at odd indices in string a are '>'. If this condition is met, it outputs 'YES', indicating a path exists; otherwise, it outputs 'NO'. The function processes multiple test cases and outputs the result for each case.

