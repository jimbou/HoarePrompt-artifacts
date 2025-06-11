#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters.
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
        
    #State: tests is an integer t (1 <= t <= 1000), i is t-1, slength is an integer equal to the input integer, a is a string equal to the second input string, b is a string equal to the third input string, c is a string equal to the fourth input string. If c is equal to a or b, or if any character in c is not present in either a or b, then 'NO' is being printed. Otherwise, no operation is performed. stdin contains 0 test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by three strings a, b, and c. It then checks if string c is equal to either a or b, or if any character in c is not present in either a or b. If either condition is true, it prints 'NO' for that test case. If neither condition is true, it prints 'YES' for that test case. The function processes all test cases and then terminates, leaving the standard input empty.

