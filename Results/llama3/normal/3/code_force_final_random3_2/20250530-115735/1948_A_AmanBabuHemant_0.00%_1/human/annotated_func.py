#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing an integer n (1 <= n <= 50).
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
        
    #State: _ is t, t is 0, n is an integer between 1 and 50, stdin contains 0 lines each containing an integer n (1 <= n <= 50). If n is odd, 'NO' is printed. If n is even, a string s of '110' repeated n // 2 times is created. If the length of s is less than 200, 'YES' is printed and the string s is printed. Otherwise, 'NO' is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the size of a string to be generated. For each even n, it generates a string s consisting of '110' repeated n // 2 times and prints 'YES' followed by the string if its length is less than 200. If n is odd or the length of s is 200 or more, it prints 'NO'. The function processes all test cases and does not return any value.

