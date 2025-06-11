#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer t (1 <= t <= 1000). The second line contains a binary string s of size n (1 <= n <= 50).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        s = input()
        
        cnt1 = s.count('1')
        
        if cnt1 > 2 and cnt1 % 2 == 0:
            print('YES')
        elif cnt1 > 2:
            print('NO')
        elif cnt1 == 1:
            print('NO')
        elif '11' in s:
            print('NO')
        else:
            print('YES')
        
    #State: t is an integer between 1 and 1000, t is 0, _ is t, n is an integer equal to the last test case, s is a string equal to the last input string, cnt1 is an integer equal to the number of '1' characters in s, stdin contains no input. If cnt1 is more than 2 and cnt1 is even, 'YES' is printed. If cnt1 is more than 2 but cnt1 is not even, 'NO' is printed. If cnt1 is 1 or '11' is in s, 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then checks the number of '1' characters in the binary string and prints 'YES' or 'NO' based on the following conditions: if the count is more than 2 and even, it prints 'YES'; if the count is more than 2 but not even, it prints 'NO'; if the count is 1 or the string contains '11', it prints 'NO'; otherwise, it prints 'YES'. The function processes all test cases and prints the corresponding results.

