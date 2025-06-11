#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case contains an integer n (1 <= n <= 20) followed by three strings a, b, c, each consisting of n lowercase Latin letters.
    tests = int(input())
    for i in range(tests):
        slength = int(input())
        
        a = input()
        
        b = input()
        
        c = input()
        
        no = True
        
        if c == a or c == b:
            no = False
            print('NO')
        else:
            for x in c:
                if x not in a and x not in b:
                    print('YES')
                    no = False
                    break
        
        if no:
            print('NO')
        
    #State: tests is 0, i is tests, stdin contains 0 test cases, slength is an integer between 1 and 20, a is a string of slength lowercase Latin letters, b is a string of slength lowercase Latin letters, c is a string of slength lowercase Latin letters. If c is equal to a or b, or if any character of c is not in a and not in b, then 'NO' is being printed. Otherwise, no is True

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three strings of lowercase Latin letters. It checks if the third string is equal to either of the first two strings or if any character in the third string is not present in both the first two strings. If either condition is true, it prints 'NO'; otherwise, it prints nothing. The function processes all test cases and then terminates, leaving the input stream empty.

