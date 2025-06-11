#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer and less or equal than 50.
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
        
    #State: The loop will execute t times, and for each iteration, it will print 'YES' or 'NO' based on the input string s. After all iterations, the loop will terminate, and the value of t will be 0.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n (less than or equal to 50) and a binary string s of the same length as n. It then checks the binary string s and prints 'YES' or 'NO' based on the following conditions: if n is 2, it prints 'YES' if s is '00', otherwise it prints 'NO'. If n is greater than 2, it prints 'NO' if the count of '1's in s is odd, or if the count of '1's is 2 and '11' appears exactly once in s. Otherwise, it prints 'YES'. The function repeats this process for each test case and terminates when all test cases have been processed.

