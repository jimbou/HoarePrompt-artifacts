#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and/or '>', where n is even.
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
        
    #State: j is t-1, n is an integer, i is n-1 if n is odd and n if n is even, a is a string, b is a string, stdin is empty, and either 'YES' or 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and two strings a and b of length n. It checks if the strings a and b satisfy a specific condition: for every pair of adjacent characters in a and b, if both characters are '<', then the function prints 'NO' and moves on to the next test case. If no such pair is found, it prints 'YES'. The function repeats this process for all test cases and then terminates, leaving the input stream empty.

