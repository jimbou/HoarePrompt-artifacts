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
        
    #State: j is t-1, t is 0, n is an integer equal to the input value and at least 3, a is a string of length n consisting of '<' and '>' characters, b is a string of length n consisting of '<' and '>' characters, i is n-1 if n is odd, otherwise i is n, stdin contains 0 test cases, and either 'YES' or 'NO' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and two strings a and b of length n containing '<' and '>' characters. It then checks each test case to determine if the strings satisfy a specific condition: for every pair of adjacent characters in the strings, if the characters are both '<', they must be in the same position in both strings. If this condition is met for all pairs of adjacent characters, the function prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and prints a result for each one.

