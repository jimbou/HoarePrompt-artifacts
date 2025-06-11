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
            counter = 0
            for x in c:
                if x not in a[counter] and x not in b[counter]:
                    no = False
                    print('YES')
                    break
                counter += 1
        
        if no:
            print('NO')
        
    #State: tests is an integer between 1 and 1000 (inclusive), i is equal to tests - 1, slength is an integer equal to the input value, a is a string equal to the first input string, b is a string equal to the second input string, c is a string equal to the third input string. If c is equal to a or b, then no is False and 'NO' is printed. Otherwise, c must have at least slength characters, and for each character in c, it must be present in either a[counter] or b[counter] for any counter less than slength. If any character in c is not present in a[counter] or b[counter] for any counter less than slength, then no is False and 'YES' is printed if no is False, and we are out of the most internal loop or if statement if no is False. If no is True, then 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by three strings a, b, and c, each of length n. It then checks if string c can be formed by taking characters from strings a and b, where each character in c must be present in either the corresponding position in a or b. If c can be formed, it prints 'NO', otherwise it prints 'YES'. The function processes all test cases and prints the result for each case.

