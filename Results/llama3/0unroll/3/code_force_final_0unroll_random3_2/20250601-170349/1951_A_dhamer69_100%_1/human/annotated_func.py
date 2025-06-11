#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer less than or equal to 50.
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
        
    #State: t is 0, and the output of each test case is printed to the console.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer (n) and a binary string (s) of the same length. It then checks each test case to determine if the binary string meets certain conditions. If the length of the binary string is 2, it checks if the string is '00' and prints 'YES' if true, otherwise 'NO'. For lengths greater than 2, it counts the number of '1's in the string and checks if this count is even. If the count is odd, it prints 'NO'. If the count is even, it further checks if the string contains exactly one '11' and the count of '1's is 2, printing 'NO' if true. In all other cases, it prints 'YES'. The function continues this process until all test cases have been processed, printing the result of each test case to the console.

