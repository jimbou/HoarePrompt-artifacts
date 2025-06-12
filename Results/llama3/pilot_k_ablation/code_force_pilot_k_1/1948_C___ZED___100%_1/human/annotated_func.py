#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. n is even.
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
        
    #State: j is equal to t, stdin is empty, n is an integer between 1 and 10^4, a is a string, b is a string, and either 'NO' has been printed for each test case where a pair of adjacent characters in a and b that are both '<' exist, or 'YES' has been printed for each test case where no such pair exists.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two strings of '<' and '>' characters. It checks for each test case whether there exists a pair of adjacent characters in the two strings that are both '<'. If such a pair exists, it prints 'NO'; otherwise, it prints 'YES'. The function processes all test cases and then terminates, leaving the standard input empty.

