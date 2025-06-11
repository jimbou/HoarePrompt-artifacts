#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (1 <= integer <= 1000) and then a binary string of the same length as the integer.
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
        
    #State: The loop has executed `t-1` times, and the output for each test case is either 'YES' or 'NO' depending on the conditions specified in the loop body. The value of `t` remains unchanged, and the input buffer (stdin) is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string of the same length. It then checks the binary string for certain conditions and prints 'YES' or 'NO' depending on whether the conditions are met. The conditions are: if the string contains no '1's, if the string contains more than two '1's and the count of '1's is even, or if the string contains exactly two '1's and they are not adjacent. If none of these conditions are met, it prints 'NO'. The function processes all test cases and prints the corresponding output for each case.

