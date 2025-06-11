#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer t (1 <= t <= 1000). The second line contains a binary string s of size n (1 <= n <= 50).
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
        
    #State: t is an integer between 1 and 1000 inclusive, i is equal to t, n is an integer equal to the input integer, a is a string equal to the input string, count is an integer equal to the number of '1' characters in a. If count is 0, 'YES' is printed. If count is greater than 2 and is even, 'YES' is printed. If count is 2 and the character after the first '1' in string a is not '1', then 'YES' is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then checks the number of '1' characters in the binary string and prints 'YES' if the count is 0, or if the count is greater than 2 and even, or if the count is 2 and the character after the first '1' is not '1'. Otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results.

