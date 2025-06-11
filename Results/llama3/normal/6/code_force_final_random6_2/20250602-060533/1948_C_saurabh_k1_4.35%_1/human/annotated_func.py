#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. n is even.
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(str, input()))
        
        b = list(map(str, input()))
        
        if b[n - 2] == str('<'):
            print('No')
        else:
            print('Yes')
        
    #State: stdin is empty, n is an integer, a is a list of strings, b is a list of strings, _ is t-1. If the second last element of list b is '<', then 'No' is printed. Otherwise, 'Yes' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and two strings of length n containing '<' and '>' characters. It then checks the second last character of the second string in each test case. If the character is '<', it prints 'No', otherwise it prints 'Yes'. The function processes all test cases and empties the standard input.

