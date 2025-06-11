#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 ≤ t ≤ 1000) and then a binary string of size t.
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
        
    #State: The output state will be a series of 'YES' or 'NO' strings, one for each test case, indicating whether the binary string in that test case meets the conditions specified in the loop. The value of `t` will remain unchanged, as it is not modified within the loop. The stdin will be empty, as all input has been consumed by the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string. It then evaluates the binary string based on specific conditions: if the count of '1's is greater than 2 and even, it prints 'YES'; if the count of '1's is greater than 2 and odd, it prints 'NO'; if the count of '1's is 1, it prints 'NO'; if the string contains '11', it prints 'NO'; otherwise, it prints 'YES'. The function processes all test cases and prints the corresponding results, leaving the input unchanged and consuming all input from standard input.

