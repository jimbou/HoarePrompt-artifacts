#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 ≤ t ≤ 1000) and then a binary string of size n (1 ≤ n ≤ 50).
    t = int(input())
    while t > 0:
        n = int(input())
        
        s = input()
        
        if n == 2:
            if s == '00':
                print('YES')
            else:
                print('NO')
        else:
            count_1 = s.count('1')
            if count_1 % 2 != 0:
                print('NO')
            elif s.count('11') == 1 and count_1 == 2:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: t is 0, n is an integer, s is a binary string of size n (1 ≤ n ≤ 50), stdin contains no test cases. If n is 2, then if s is '00', 'YES' is printed. Otherwise, 'NO' is printed. If n is not 2, then if count_1 is odd, 'NO' is printed. If count_1 is even, then if s contains exactly one occurrence of the substring '11' and count_1 is 2, 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a binary string s of size n. It then checks the string s based on its length n and the count of '1's in the string. If n is 2, it prints 'YES' if the string is '00', otherwise it prints 'NO'. If n is not 2, it prints 'NO' if the count of '1's is odd, or if the string contains exactly one '11' and the count of '1's is 2. In all other cases, it prints 'YES'. The function continues this process until all test cases have been read from standard input.

