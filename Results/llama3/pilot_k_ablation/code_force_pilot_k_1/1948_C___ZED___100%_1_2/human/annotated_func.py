#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and/or '>'. n is even.
    for j in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('NO')
                break
        else:
            print('YES')
        
    #State: `j` is `t`, `stdin` is empty, `n` is an integer, `a` is a string, `b` is a string, `i` is either `n-1` if `n` is odd or `n-2` if `n` is even, and either 'NO' or 'YES' has been printed for each test case. If 'NO' has been printed for a test case, then there exists an `i` in the range 1 to `n-1` (inclusive) such that `a[i] == b[i + 1] == '<'` or `a[i] == b[i - 1] == '<'`. If 'YES' has been printed for a test case, then no such `i` exists.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by two strings of length n containing '<' and/or '>'. It then checks each test case to determine if there exists a pair of adjacent characters in the strings that are both '<'. If such a pair is found, it prints 'NO' for that test case; otherwise, it prints 'YES'. The function processes all test cases and prints a result for each one, leaving the input stream empty and the variables n, a, and b with their final values from the last test case.

