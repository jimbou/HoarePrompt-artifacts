#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n >= m and (n - m) % 2 == 0:
            print('YES')
        else:
            print('NO')
        
    #State: The output will be a series of 'YES' or 'NO' printed to the console, each corresponding to whether the difference between n and m is even for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers n and m. It then determines whether the difference between n and m is even for each test case and prints 'YES' if it is, or 'NO' if it is not. The function processes multiple test cases and prints a corresponding 'YES' or 'NO' for each case.

