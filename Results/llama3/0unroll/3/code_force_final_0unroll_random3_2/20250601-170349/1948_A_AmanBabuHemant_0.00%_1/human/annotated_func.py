#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a sequence of integers (the number of special characters in each test case). Each integer is between 1 and 50 (inclusive).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n % 2:
            print('NO')
        else:
            s = '110' * (n // 2)
            if len(s) < 200:
                print('YES')
                print(s)
            else:
                print('NO')
        
    #State: The output state will contain a sequence of 'YES' or 'NO' for each test case, followed by a string of '110' repeated n/2 times if the number of special characters is even and less than 200. If the number of special characters is odd or 200 or more, the output will be 'NO'. The value of t will remain unchanged.

#Overall this is what the function does:This function reads a sequence of test cases from standard input, where each test case is an integer representing the number of special characters. It then determines whether the number of special characters is even and less than 200. If it is, the function prints 'YES' followed by a string of '110' repeated n/2 times. If the number of special characters is odd or 200 or more, the function prints 'NO'. The function processes multiple test cases and prints the result for each case.

