#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (the number of special characters for each test case). Each integer is greater than or equal to 1 and less than or equal to 50.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            print('YES')
            pattern = []
            for i in range(n // 2):
                pattern.append('AB'[i % 2])
                pattern.append('AB'[i % 2 ^ 1])
            print(''.join(pattern))
        
    #State: Output State: The output state after the loop executes all the iterations is a sequence of strings, where each string is either 'YES' or 'NO', followed by a pattern of 'A's and 'B's if the corresponding input number is even. The number of 'YES' or 'NO' strings is equal to the initial value of `t`, and the length of each pattern is equal to the corresponding input number. The value of `t` is unchanged.

#Overall this is what the function does:This function reads a sequence of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents the number of special characters for each test case. For each test case, if the number of special characters is odd, it prints 'NO'. If the number of special characters is even, it prints 'YES' followed by a pattern of alternating 'A's and 'B's of the same length as the number of special characters. The function repeats this process for the specified number of test cases, producing a sequence of 'YES' or 'NO' strings, potentially followed by patterns of 'A's and 'B's.

