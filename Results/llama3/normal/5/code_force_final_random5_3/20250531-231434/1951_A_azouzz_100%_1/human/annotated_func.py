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
        
    #State: _ is equal to t, t is an integer between 1 and 1000, n is an integer, s is a binary string of size n, cnt1 is an integer equal to the number of '1' characters in s, and stdin contains no input. If cnt1 is more than 2 and cnt1 is even, 'YES' is printed. If cnt1 is more than 2 and cnt1 is odd, 'NO' is printed. If cnt1 is 1, 'NO' is printed. If cnt1 is 2, then if '11' is in s, 'NO' is printed; otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then checks the number of '1' characters in the binary string and prints 'YES' or 'NO' based on specific conditions: if the count is more than 2 and even, it prints 'YES'; if the count is more than 2 and odd, it prints 'NO'; if the count is 1, it prints 'NO'; and if the count is 2, it prints 'NO' if the string contains '11', otherwise it prints 'YES'. The function processes all test cases and then terminates, leaving the standard input empty.

