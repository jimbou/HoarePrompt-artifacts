#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and/or '>' characters. n is even.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('No')
                break
        else:
            print('yes')
        
    #State: t is an integer between 1 and 10^4 inclusive and greater than or equal to 0, n is an integer, a is a string, b is a string, _ is t, stdin contains 0 test cases, i is n if n is odd, otherwise i is n-1. If for all i in range(1, n, 2), neither a[i] == b[i + 1] == '<' nor a[i] == b[i - 1] == '<' is true, then 'yes' is printed. Otherwise, 'No' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by two strings of length n containing '<' and '>' characters. It then checks if the strings satisfy a certain condition: for every pair of characters at odd indices, neither the current character in the first string nor the previous character in the second string can be '<'. If this condition is met for all pairs, it prints 'yes'; otherwise, it prints 'No'. The function processes all test cases and prints the corresponding results.

