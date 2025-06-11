#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of three lines: the first line contains a single integer n (2 <= n <= 2 * 10^5 and n is even), the second line contains a string of exactly n characters '<' and/or '>', and the third line contains a string of exactly n characters '<' and/or '>'. The sum of n over all test cases doesn't exceed 2 * 10^5.
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
        
    #State: The output state will contain multiple lines, each containing either 'YES' or 'NO', depending on whether a path exists from the first character of the first string to the last character of the second string. The number of lines will be equal to the number of test cases.

#Overall this is what the function does:Determines whether a path exists from the first character of the first string to the last character of the second string for multiple test cases, and outputs 'YES' or 'NO' accordingly.

