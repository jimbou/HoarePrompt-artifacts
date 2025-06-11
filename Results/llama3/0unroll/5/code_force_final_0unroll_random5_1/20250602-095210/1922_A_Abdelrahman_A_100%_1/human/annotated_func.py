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
        
    #State: The loop has executed all the iterations, and the output state is a series of 'YES' or 'NO' printed to the console, depending on whether the string 'c' can be formed by taking characters from strings 'a' and 'b' at the same position. The value of 'tests' remains unchanged, and the stdin is empty after consuming all the test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three strings a, b, and c. It checks if string c can be formed by taking characters from strings a and b at the same position. If c can be formed, it prints 'YES', otherwise it prints 'NO'. The function processes all test cases and prints the corresponding results to the console.

