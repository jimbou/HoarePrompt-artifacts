#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t test cases. Each test case consists of an integer n (1 <= n <= 50) followed by a string of n characters. The string contains only '.', '@', and '*' characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first character of the string is '.'.
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: a is 0, d is an integer, b is a string of d characters containing only '.', '@', and '*' characters, j is d-1, s is 0, i is a, stdin contains 0 test cases, and the number of '@' characters in the string b which is s is being printed

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a string of n characters. It then counts the number of '@' characters in each string and prints the count. The function repeats this process until all test cases have been read from standard input.

