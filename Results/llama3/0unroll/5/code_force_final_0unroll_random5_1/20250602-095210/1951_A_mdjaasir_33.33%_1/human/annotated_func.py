#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (between 1 and 1000) and then a binary string of the same length as the integer.
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
            if a.index('1') and a[a.index('1') + 1] != '1':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
        
    #State: The loop will print 'YES' or 'NO' for each test case in the input, indicating whether the binary string can be rearranged into a palindrome or not. The value of `t` remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer and a binary string of the same length. It then determines whether the binary string can be rearranged into a palindrome and prints 'YES' or 'NO' for each test case accordingly. The function does not modify the input values and only prints the results for each test case.

