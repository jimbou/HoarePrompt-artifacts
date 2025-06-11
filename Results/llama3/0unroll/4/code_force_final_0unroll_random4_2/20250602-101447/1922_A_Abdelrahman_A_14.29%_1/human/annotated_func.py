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
        
    #State: The output state is a series of 'YES' or 'NO' printed to the console, each corresponding to a test case. For each test case, if string 'c' is equal to either 'a' or 'b', 'NO' is printed. Otherwise, if any character in 'c' is not present in both 'a' and 'b', 'YES' is printed. If neither condition is met, 'NO' is printed. The value of 'tests' remains unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three strings a, b, and c. It then checks each test case and prints 'YES' to the console if string c contains a character not present in both strings a and b, or if string c is equal to either string a or string b, it prints 'NO'. If neither condition is met, it also prints 'NO'. The function processes all test cases and does not return any value, only printing the results to the console.

