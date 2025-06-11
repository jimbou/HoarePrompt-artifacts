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
        
    #State: tests is 0, i is equal to the initial value of tests, slength is an integer equal to the last input value, a is a string equal to the second last input value, b is a string equal to the third last input value, c is a string equal to the fourth last input value, stdin is empty, no is False if any of the strings c is not equal to a or b and has at least one character not present in the corresponding index of a and b, otherwise no is True. If no is True, 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by three strings a, b, and c, each of length n. It then checks each test case to see if string c can be formed by taking one character from either string a or string b at each corresponding index. If string c can be formed in this way, the function prints 'NO'; otherwise, it prints 'YES'. The function continues this process until all test cases have been read from standard input.

