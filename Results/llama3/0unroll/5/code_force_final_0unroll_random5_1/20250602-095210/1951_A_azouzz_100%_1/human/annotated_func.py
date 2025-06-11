#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer and then a binary string of the same length as the integer. The integer is a positive integer less than or equal to 50.
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
        
    #State: The loop has executed `t` times, where `t` is a positive integer less than or equal to 50. For each iteration, the loop has read an integer `n` and a binary string `s` from stdin, and printed either 'YES' or 'NO' to stdout based on the conditions specified in the loop body. The values of `t`, `n`, and `s` have been updated for each iteration, but their initial values are no longer available. The output state only contains the results of the loop executions, which are the printed 'YES' or 'NO' values for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a positive integer n and a binary string s of length n. It then checks the binary string s based on the following conditions: if the count of '1's in s is greater than 2 and even, it prints 'YES'; if the count of '1's is greater than 2 but odd, it prints 'NO'; if the count of '1's is 1, it prints 'NO'; if the string contains '11', it prints 'NO'; otherwise, it prints 'YES'. The function repeats this process for each test case and outputs the results to standard output.

