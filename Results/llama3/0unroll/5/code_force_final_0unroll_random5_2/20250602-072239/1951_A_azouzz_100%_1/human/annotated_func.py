#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (between 1 and 1000) and then a binary string of the same length as the integer.
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
        
    #State: The loop will execute t times, and for each iteration, it will print 'YES' or 'NO' to the console based on the conditions specified in the loop body. The value of t will remain unchanged, and the stdin will be empty after all test cases have been processed. The output will be a series of 'YES' or 'NO' strings, one for each test case, indicating whether the binary string meets the specified conditions.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string of the same length. It then checks the binary string against certain conditions and prints 'YES' or 'NO' to the console for each test case, indicating whether the string meets the conditions. The function processes all test cases and empties the standard input, leaving behind a series of 'YES' or 'NO' outputs.

