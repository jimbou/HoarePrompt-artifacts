#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer less than or equal to 50.
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
        
    #State: The loop has executed all the iterations and the output state is a series of 'YES' or 'NO' strings, each corresponding to a test case, indicating whether the binary string in that test case meets the specified conditions. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer and a binary string of the same length. It then checks each binary string against specific conditions: if the string contains no '1's, an even number of '1's greater than 2, or exactly two '1's that are not adjacent, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and outputs a series of 'YES' or 'NO' strings, one for each test case, indicating whether the corresponding binary string meets the specified conditions.

