#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= n <= 50) and then a binary string of size n.
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
        
    #State: _t is an integer larger than or equal to 0, _ is t, n is an integer between 1 and 50 inclusive and equal to the integer value of the input, s is a binary string of size n and equal to the string value of the input, cnt1 is the number of '1' in s, stdin contains multiple test cases - 0 test cases. If cnt1 > 2 and cnt1 is even, 'YES' is printed. If cnt1 is 1 or cnt1 > 2 and cnt1 is odd, 'NO' is printed. If cnt1 is 2, then if '11' is in s, 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a binary string s of size n. It then checks the number of '1's in the string and prints 'YES' or 'NO' based on the following conditions: if the number of '1's is greater than 2 and even, it prints 'YES'; if the number of '1's is 1 or greater than 2 and odd, it prints 'NO'; if the number of '1's is 2, it prints 'NO' if the string contains '11', otherwise it prints 'YES'. The function processes all test cases and prints the corresponding results.

