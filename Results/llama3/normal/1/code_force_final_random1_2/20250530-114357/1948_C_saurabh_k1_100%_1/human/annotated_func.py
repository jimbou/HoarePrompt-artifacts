#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. n is even.
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
        
    #State: t is an integer between 0 and 10^4 (inclusive), stdin contains 0 test cases, n is an integer at least 2, a is a string of length n consisting of '<' and '>' characters, b is a string of length n consisting of '<' and '>' characters, _ is t-1, i is n-1 if n is odd, n if n is even. If no 'No' was printed, then 'yes' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an even-length string of '<' and '>' characters. It then checks if the strings can be rearranged to form a valid sequence of '<' and '>' characters, and prints 'yes' if possible and 'no' otherwise. The function processes all test cases and prints the result for each case.

