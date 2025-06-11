#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (2 <= n <= 2 * 10^5) followed by two strings of length n consisting of '<' and '>' characters. n is even. The sum of n over all test cases doesn't exceed 2 * 10^5.
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
        
    #State: The output state will contain 'YES' or 'NO' for each test case, indicating whether the given strings satisfy the condition or not. The 'YES' or 'NO' will be printed on separate lines, with the number of lines equal to the number of test cases (t). The input state remains unchanged, with the same values for t, n, a, and b.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and two strings of length n containing '<' and '>' characters. It then checks if the strings satisfy a specific condition, printing 'YES' if they do and 'NO' if they don't. The function processes multiple test cases and prints the result for each case on a separate line, without modifying the input values.

