#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer t (1 <= t <= 1000). The second line contains a binary string s of size n (1 <= n <= 50).
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
        
    #State: The loop will have printed 'YES' or 'NO' for each test case, indicating whether the binary string can be rearranged to have no consecutive 1s. The value of `t` will be unchanged, and the stdin will be empty after reading all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then determines whether the binary string can be rearranged to have no consecutive 1s and prints 'YES' or 'NO' for each test case accordingly. The function does not return any value and only prints the results to the standard output.

