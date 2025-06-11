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
        
    #State: The output state is a series of 'YES' or 'NO' printed to the console, with each 'YES' or 'NO' corresponding to a test case. The number of 'YES' or 'NO' printed is equal to the number of test cases, which is between 1 and 1000 inclusive. The value of the variable 'tests' remains unchanged, still being an integer between 1 and 1000 inclusive. The stdin is empty as all the test cases have been read and processed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by three strings a, b, and c. It then checks if string c contains any characters not present in strings a and b. If such a character is found, it prints 'YES' to the console; otherwise, it prints 'NO'. The function processes all test cases and prints a corresponding 'YES' or 'NO' for each case, without modifying the input variables.

