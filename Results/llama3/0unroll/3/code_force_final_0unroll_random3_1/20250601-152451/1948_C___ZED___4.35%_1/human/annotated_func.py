#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer (greater than 1), then two strings of the same length as the integer. The strings contain only '<' and '>' characters. The integer is even.
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
        
    #State: The output state will contain multiple lines of output, each corresponding to a test case. For each test case, if the last but one character of the second string is not '>', the output will be 'NO'. If the length of the strings is 1, the output will be 'YES'. Otherwise, the output will be 'YES' if there is a path from the first string to the second string by moving two characters at a time, and 'NO' otherwise.

#Overall this is what the function does:Determines the existence of a path between two strings of '<' and '>' characters by moving two characters at a time, and outputs 'YES' or 'NO' for each test case based on the presence or absence of such a path, considering the constraints of the input strings' length and the last but one character of the second string.

