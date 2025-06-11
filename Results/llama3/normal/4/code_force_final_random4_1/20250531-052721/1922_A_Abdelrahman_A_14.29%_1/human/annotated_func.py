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
        
    #State: tests is an integer between 1 and 1000 (inclusive), stdin contains 0 test cases, each test case consists of an integer n (1 <= n <= 20) followed by three strings a, b, and c, each consisting of exactly n lowercase Latin letters, i is tests - 1, slength is an integer between 1 and 20 (inclusive), a is a string consisting of exactly slength lowercase Latin letters, b is a string consisting of exactly slength lowercase Latin letters, c is a string consisting of exactly slength lowercase Latin letters. If c is equal to a or b, then 'NO' is printed. If c is not equal to a or b and the last character of c is in either a or b, then 'NO' is printed. If c is not equal to a or b and the last character of c is not in either a or b, then 'YES' is printed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by three strings a, b, and c, each of length n. It then checks if string c is equal to either a or b, or if any character in c is present in either a or b. If either condition is true, it prints 'NO', otherwise it prints 'YES'. The function processes all test cases and prints the corresponding results.

