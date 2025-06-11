#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer t (1 <= t <= 1000) representing the number of test cases. The second line contains an integer n (1 <= n <= 50) representing the number of lamps, followed by a binary string s of size n representing the final desired configuration.
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
            elif s.count('11') == 1:
                print('NO')
            else:
                print('YES')
        
        t -= 1
        
    #State: t is 0, and the output of the program is a series of 'YES' or 'NO' for each test case.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a number of lamps and a binary string representing the desired configuration. It then determines whether the desired configuration can be achieved and prints 'YES' or 'NO' for each test case. The function repeats this process until all test cases have been processed, at which point it concludes, leaving the output as a series of 'YES' or 'NO' responses.

